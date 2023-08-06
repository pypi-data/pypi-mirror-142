"""
Manipulation of textual data.
"""

import collections.abc
import copy
import difflib
import os
import pathlib
import re
import string
import subprocess

import numpy as np
import pandas as pd

from ._cache import _ENGLISH_WRITTEN_NUMBERS
from .ops import dict_to_dataframe, find_executable

""" == Basic processing of textual data ====================================================== """


def get_acronym(text, only_capitals=False, capitals_in_words=False):
    """
    Get an acronym (in capital letters) of an input text.

    :param text: any text
    :type text: str
    :param only_capitals: whether to include capital letters only, defaults to ``False``
    :type only_capitals: bool
    :param capitals_in_words: whether to include all captical letters in a single word,
        defaults to ``False``
    :type capitals_in_words: bool
    :return: acronym of the input ``str_var``
    :rtype: str

    **Examples**::

        >>> from pyhelpers.text import get_acronym

        >>> text_a = 'This is an apple.'
        >>> acron = get_acronym(text_a)
        >>> acron
        'TIAA'

        >>> text_b = "I'm at the University of Birmingham."
        >>> acron = get_acronym(text_b, only_capitals=True)
        >>> acron
        'IUB'

        >>> text_c = 'There is a "ConnectionError"!'
        >>> acron = get_acronym(text_c, capitals_in_words=True)
        >>> acron
        'TCE'
    """

    txt = remove_punctuation(text)

    if only_capitals:
        acronym = ''.join(x[0] for x in txt.split() if x[0].isupper())
    elif capitals_in_words:
        acronym = ''.join(list(filter(str.isupper, txt)))
    else:
        acronym = ''.join(x[0].upper() for x in txt.split())

    return acronym


def remove_punctuation(x, rm_whitespace=True):
    """
    Remove punctuation from string-type data.

    :param x: raw string-type data
    :type x: str
    :param rm_whitespace: whether to remove whitespace, defaults to ``True``
    :type rm_whitespace: bool
    :return: text with punctuation removed
    :rtype: str

    **Examples**::

        >>> from pyhelpers.text import remove_punctuation

        >>> raw_text = 'Hello\tworld! This is a test. :-)'

        >>> text = remove_punctuation(raw_text)
        >>> text
        'Hello\tworld  This is a test'

        >>> text = remove_punctuation(raw_text, rm_whitespace=True)
        >>> text
        'Hello world This is a test'
    """

    x_ = re.sub(r'[^\w\s]', ' ', x)

    # noinspection PyBroadException
    try:
        y = x_.translate(str.maketrans('', '', string.punctuation))
    except Exception:
        y = ''.join(y_ for y_ in x_ if y_ not in string.punctuation)

    z = y.strip()

    if rm_whitespace:
        z = ' '.join(z.split())

    return z


def extract_words1upper(x, join_with=None):
    """
    Extract words from a string by spliting it at occurrence of an uppercase letter.

    :param x: a string joined by a number of words each starting with an uppercase letter
    :type x: str
    :param join_with: a string with which to (re)join the single words, defaults to ``None``
    :type join_with: str or None
    :return: a list of single words each starting with an uppercase letter,
        or a single string joined together by them with ``join_with``
    :rtype: list or str

    **Examples**::

        >>> from pyhelpers.text import extract_words1upper

        >>> x1 = 'NetworkWaymarks'
        >>> res = extract_words1upper(x1, join_with=' ')
        >>> res
        'Network Waymarks'

        >>> x2 = 'Retaining_Wall'
        >>> res = extract_words1upper(x2, join_with=' ')
        >>> res
        'Retaining Wall'
    """

    y = remove_punctuation(x)

    # re.sub(r"([A-Z])", r" \1", x).split()
    extracted_words = re.findall(r'[a-zA-Z][^A-Z]*', y)

    if join_with:
        extracted_words = join_with.join(extracted_words)

    return extracted_words


def numeral_english_to_arabic(x):
    """
    Convert a string which potentially is a number written in English to an Arabic number

    :param x: a number written in English
    :type x: str
    :return: a number written in Arabic
    :rtype: int

    **Examples**::

        >>> from pyhelpers.text import numeral_english_to_arabic

        >>> numeral_english_to_arabic('one')
        1

        >>> numeral_english_to_arabic('one hundred and one')
        101

        >>> numeral_english_to_arabic('a thousand two hundred and three')
        1203

        >>> numeral_english_to_arabic('200 and five')
        205

        >>> numeral_english_to_arabic('Two hundred and fivety')  # Two hundred and fifty
        Exception: Illegal word: "fivety"
    """

    current = result = 0

    for word in x.lower().replace('-', ' ').split():
        if word not in _ENGLISH_WRITTEN_NUMBERS and not word.isdigit():
            # word_ = find_similar_str(word, ENGLISH_WRITTEN_NUMBERS)
            # if word_ is None:
            raise Exception(f"Illegal word: \"{word}\"")
            # else:
            #     word = word_

        if word.isdigit():
            scale, increment = (1, int(word))
        else:
            scale, increment = _ENGLISH_WRITTEN_NUMBERS[word]
        current = current * scale + increment

        if scale > 100:
            result += current
            current = 0

    return result + current


""" == Comparison of textual data ============================================================ """


def find_matched_str(x, lookup_list):
    """
    Find all that are matched with a string from among a sequence of strings.

    :param x: a string-type variable
    :type x: str
    :param lookup_list: a sequence of strings for lookup
    :type lookup_list: typing.List[str] or typing.Tuple[str] or typing.Sequence[str]
    :return: a generator containing all that are matched with ``x``
    :rtype: typing.Generator or None

    **Examples**::

        >>> from pyhelpers.text import find_matched_str

        >>> lookup_lst = ['abc', 'aapl', 'app', 'ap', 'ape', 'apex', 'apel']
        >>> res = find_matched_str('apple', lookup_lst)
        >>> list(res)
        []

        >>> lookup_lst += ['apple']
        >>> lookup_lst
        ['abc', 'aapl', 'app', 'ap', 'ape', 'apex', 'apel', 'apple']

        >>> res = find_matched_str('apple', lookup_lst)
        >>> list(res)
        ['apple']

        >>> res = find_matched_str(r'app(le)?', lookup_lst)
        >>> list(res)
        ['app', 'apple']
    """

    if x is not None:
        for y in lookup_list:
            if re.match(x, y, re.IGNORECASE):
                yield y


def find_similar_str(x, lookup_list, n=1, ignore_punctuation=True, method='difflib', **kwargs):
    """
    From among a sequence of strings, find ``n`` ones that are similar to ``x``.

    :param x: a string-type variable
    :type x: str
    :param lookup_list: a sequence of strings for lookup
    :type lookup_list: typing.List[str] or typing.Tuple[str] or typing.Sequence[str]
    :param n: number of similar strings to return, defaults to ``1``;
        if ``n=None``, the function returns a sorted ``lookup_list`` (in descending order of similarity)
    :type n: int or None
    :param method: options include ``'difflib'`` (default) and ``'fuzzywuzzy'``

        - if ``method='difflib'``, the function relies on `difflib.get_close_matches`_
        - if ``method='fuzzywuzzy'``, the function relies on `fuzzywuzzy.fuzz.token_set_ratio`_

    :type method: str or None

    :param ignore_punctuation: whether to ignore puctuations in the search for similar texts
    :type ignore_punctuation: bool
    :param kwargs: [optional] parameters of `difflib.get_close_matches`_ or
        `fuzzywuzzy.fuzz.token_set_ratio`_, depending on ``processor``
    :return: a string-type variable that should be similar to (or the same as) ``x``
    :rtype: str or list or None

    .. _`difflib.get_close_matches`:
        https://docs.python.org/3/library/difflib.html#difflib.get_close_matches
    .. _`fuzzywuzzy.fuzz.token_set_ratio`:
        https://github.com/seatgeek/fuzzywuzzy

    **Examples**::

        >>> from pyhelpers.text import find_similar_str

        >>> lookup_lst = ['Anglia',
        ...               'East Coast',
        ...               'East Midlands',
        ...               'North and East',
        ...               'London North Western',
        ...               'Scotland',
        ...               'South East',
        ...               'Wales',
        ...               'Wessex',
        ...               'Western']

        >>> str_similar = find_similar_str(x='angle', lookup_list=lookup_lst)
        >>> str_similar
        'Anglia'
        >>> str_similar = find_similar_str(x='angle', lookup_list=lookup_lst, method='fuzzywuzzy')
        >>> str_similar
        'Anglia'

        >>> str_similar = find_similar_str(x='x', lookup_list=lookup_lst)
        >>> str_similar  # None

        >>> str_similar = find_similar_str(x='x', lookup_list=lookup_lst, method='fuzzywuzzy')
        >>> str_similar
        'Wessex'
    """

    assert method in ('difflib', 'fuzzywuzzy', None), \
        "Options for `processor` include \"difflib\" and \"fuzzywuzzy\"."

    m = len(lookup_list) if n is None else copy.copy(n)

    if method in {'difflib', None}:
        x_ = x.lower()
        lookup_dict = {y.lower(): y for y in lookup_list}

        if ignore_punctuation:
            x_ = remove_punctuation(x_)
            lookup_dict = {remove_punctuation(k): v for k, v in lookup_dict.items()}

        sim_str_ = difflib.get_close_matches(word=x_, possibilities=lookup_dict.keys(), n=m, **kwargs)

        if not sim_str_:
            sim_str = None
        else:
            sim_str = lookup_dict[sim_str_[0]]

    elif method == 'fuzzywuzzy':
        import fuzzywuzzy.fuzz

        l_distances = [fuzzywuzzy.fuzz.token_set_ratio(s1=x, s2=a, **kwargs) for a in lookup_list]

        if sum(l_distances) == 0:
            sim_str = None
        else:
            if m == 1:
                sim_str = lookup_list[l_distances.index(max(l_distances))]
            else:
                sim_str = [lookup_list[i] for i in np.argsort(l_distances)[::-1]][:m]

    else:
        sim_str = None

    return sim_str


""" == Basic computation of textual data ===================================================== """


def count_words(raw_txt):
    """
    Count the total for each different word.

    :param raw_txt: any text
    :type raw_txt: str
    :return: number of each word in ``raw_docs``
    :rtype: dict

    **Examples**::

        >>> from pyhelpers.text import count_words, remove_punctuation

        >>> raw_text = 'This is an apple. That is a pear. Hello world!'

        >>> count_words(raw_text)
        {'This': 1,
         'is': 2,
         'an': 1,
         'apple': 1,
         '.': 2,
         'That': 1,
         'a': 1,
         'pear': 1,
         'Hello': 1,
         'world': 1,
         '!': 1}

        >>> count_words(remove_punctuation(raw_text))
        {'This': 1,
         'is': 2,
         'an': 1,
         'apple': 1,
         'That': 1,
         'a': 1,
         'pear': 1,
         'Hello': 1,
         'world': 1}
    """

    import nltk

    doc_text = str(raw_txt)
    tokens = nltk.word_tokenize(doc_text)

    word_count_dict = dict(collections.Counter(tokens))

    return word_count_dict


def calculate_idf(raw_documents, rm_punc=False):
    """
    Calculate inverse document frequency.

    :param raw_documents: a series of documents
    :type raw_documents: pandas.Series
    :param rm_punc: whether to remove punctuation from ``raw_documents``, defaults to ``False``
    :type rm_punc: bool
    :return: term frequency (TF) of ``raw_documents``, and inverse document frequency
    :rtype: tuple

    **Examples**::

        >>> from pyhelpers.text import calculate_idf
        >>> import pandas

        >>> raw_doc_ = [
        ...     'This is an apple.',
        ...     'That is a pear.',
        ...     'It is human being.',
        ...     'Hello world!']
        >>> raw_doc = pandas.Series(raw_doc_)

        >>> docs_tf_, corpus_idf_ = calculate_idf(raw_doc, rm_punc=False)
        >>> docs_tf_
        0    {'This': 1, 'is': 1, 'an': 1, 'apple': 1, '.': 1}
        1      {'That': 1, 'is': 1, 'a': 1, 'pear': 1, '.': 1}
        2    {'It': 1, 'is': 1, 'human': 1, 'being': 1, '.'...
        3                     {'Hello': 1, 'world': 1, '!': 1}
        dtype: object

        >>> corpus_idf_
        {'This': 0.6931471805599453,
         'is': 0.0,
         'an': 0.6931471805599453,
         'apple': 0.6931471805599453,
         '.': 0.0,
         'That': 0.6931471805599453,
         'a': 0.6931471805599453,
         'pear': 0.6931471805599453,
         'It': 0.6931471805599453,
         'human': 0.6931471805599453,
         'being': 0.6931471805599453,
         'Hello': 0.6931471805599453,
         'world': 0.6931471805599453,
         '!': 0.6931471805599453}

        >>> docs_tf_, corpus_idf_ = calculate_idf(raw_doc, rm_punc=True)
        >>> docs_tf_
        0     {'This': 1, 'is': 1, 'an': 1, 'apple': 1}
        1       {'That': 1, 'is': 1, 'a': 1, 'pear': 1}
        2    {'It': 1, 'is': 1, 'human': 1, 'being': 1}
        3                      {'Hello': 1, 'world': 1}
        dtype: object

        >>> corpus_idf_
        {'This': 0.6931471805599453,
         'is': 0.0,
         'an': 0.6931471805599453,
         'apple': 0.6931471805599453,
         'That': 0.6931471805599453,
         'a': 0.6931471805599453,
         'pear': 0.6931471805599453,
         'It': 0.6931471805599453,
         'human': 0.6931471805599453,
         'being': 0.6931471805599453,
         'Hello': 0.6931471805599453,
         'world': 0.6931471805599453}
    """

    assert isinstance(raw_documents, pd.Series)

    raw_docs = raw_documents.copy()
    if rm_punc:
        raw_docs = raw_docs.map(remove_punctuation)

    docs_tf = raw_docs.map(count_words)
    tokens_in_docs = docs_tf.map(lambda x: list(x.keys()))

    n = len(raw_docs)
    tokens = [w for tokens in tokens_in_docs for w in tokens]
    tokens_counter = dict_to_dataframe(dict(collections.Counter(tokens)), 'token', 'count')
    tokens_counter['idf'] = np.log(n / (1 + tokens_counter['count'].values))

    corpus_idf = dict(zip(tokens_counter['token'], tokens_counter['idf']))

    return docs_tf, corpus_idf


def calculate_tf_idf(raw_documents, rm_punc=False):
    """
    Count term frequency–inverse document frequency.

    :param raw_documents: a series of documents
    :type raw_documents: pandas.Series
    :param rm_punc: whether to remove punctuation from ``raw_documents``, defaults to ``False``
    :type rm_punc: bool
    :return: tf-idf of the ``raw_documents``
    :rtype: dict

    **Examples**::

        >>> from pyhelpers.text import calculate_tf_idf
        >>> import pandas

        >>> raw_doc_ = [
        ...     'This is an apple.',
        ...     'That is a pear.',
        ...     'It is human being.',
        ...     'Hello world!']
        >>> raw_doc = pandas.Series(raw_doc_)

        >>> docs_tf_idf_ = calculate_tf_idf(raw_doc, rm_punc=False)
        >>> docs_tf_idf_
        0    {'This': 0.6931471805599453, 'is': 0.0, 'an': ...
        1    {'That': 0.6931471805599453, 'is': 0.0, 'a': 0...
        2    {'It': 0.6931471805599453, 'is': 0.0, 'human':...
        3    {'Hello': 0.6931471805599453, 'world': 0.69314...
        dtype: object

        >>> docs_tf_idf_ = calculate_tf_idf(raw_doc, rm_punc=True)
        >>> docs_tf_idf_
        0    {'This': 0.6931471805599453, 'is': 0.0, 'an': ...
        1    {'That': 0.6931471805599453, 'is': 0.0, 'a': 0...
        2    {'It': 0.6931471805599453, 'is': 0.0, 'human':...
        3    {'Hello': 0.6931471805599453, 'world': 0.69314...
        dtype: object
    """

    docs_tf, corpus_idf = calculate_idf(raw_documents=raw_documents, rm_punc=rm_punc)

    docs_tf_idf = docs_tf.apply(
        lambda x: {k: v * corpus_idf[k] for k, v in x.items() if k in corpus_idf})

    return docs_tf_idf


def euclidean_distance_between_texts(txt1, txt2):
    """
    Compute Euclidean distance of two sentences.

    :param txt1: any text
    :type txt1: str
    :param txt2: any text
    :type txt2: str
    :return: Euclidean distance between ``txt1`` and ``txt2``
    :rtype: float

    **Example**::

        >>> from pyhelpers.text import euclidean_distance_between_texts

        >>> txt_1, txt_2 = 'This is an apple.', 'That is a pear.'

        >>> e_dist = euclidean_distance_between_texts(txt_1, txt_2)
        >>> e_dist
        2.6457513110645907
    """

    if isinstance(txt1, str) and isinstance(txt2, str):
        doc_words = set(txt1.split() + txt2.split())

    else:
        assert isinstance(txt1, list), isinstance(txt2, list)
        doc_words = set(txt1 + txt2)

    s1_count, s2_count = [], []
    for word in doc_words:
        s1_count.append(txt1.count(word))
        s2_count.append(txt2.count(word))

    # ed = np.sqrt(np.sum((np.array(s1_count) - np.array(s2_count)) ** 2))
    ed = np.linalg.norm(np.array(s1_count) - np.array(s2_count))

    return ed


def cosine_similarity_between_texts(txt1, txt2, cosine_distance=False):
    """
    Calculate cosine similarity of two sentences.

    :param txt1: any text
    :type txt1: str
    :param txt2: any text
    :type txt2: str
    :param cosine_distance: whether to get cosine distance, which is (1 - cosine similarity),
        defaults to ``False``
    :type cosine_distance: bool
    :return: cosine similarity (or distance)
    :rtype: float

    **Examples**::

        >>> from pyhelpers.text import cosine_similarity_between_texts

        >>> txt_1, txt_2 = 'This is an apple.', 'That is a pear.'

        >>> cos_sim = cosine_similarity_between_texts(txt_1, txt_2)
        >>> cos_sim
        0.6963106238227914

        >>> cos_dist = cosine_similarity_between_texts(txt_1, txt_2, cosine_distance=True)
        >>> cos_dist  # 1 - cos_sim
        0.3036893761772086
    """

    if isinstance(txt1, str) and isinstance(txt2, str):
        doc_words = set(txt1.split() + txt2.split())

    else:
        assert isinstance(txt1, list), isinstance(txt2, list)
        doc_words = set(txt1 + txt2)

    s1_count, s2_count = [], []
    for word in doc_words:
        s1_count.append(txt1.count(word))
        s2_count.append(txt2.count(word))

    s1_count, s2_count = np.array(s1_count), np.array(s2_count)

    similarity = np.dot(s1_count, s2_count)
    cos_similarity = np.divide(similarity, np.linalg.norm(s1_count) * np.linalg.norm(s2_count))

    if cosine_distance:
        cos_similarity = 1 - cos_similarity

    return cos_similarity


""" == Conversion of text files ============================================================== """


def convert_md_to_rst(path_to_md, path_to_rst, verbose=False, pandoc_exe=None, **kwargs):
    """
    Convert a `Markdown <https://daringfireball.net/projects/markdown/>`_ file (.md)
    to a `reStructuredText <https://docutils.readthedocs.io/en/sphinx-docs/user/rst/quickstart.html>`_
    (.rst) file.

    This function relies on
    `Pandoc <https://pandoc.org/>`_ or `pypandoc <https://github.com/bebraw/pypandoc>`_.

    :param path_to_md: path where a markdown file is saved
    :type path_to_md: str
    :param path_to_rst: path where a reStructuredText file is saved
    :type path_to_rst: str
    :param verbose: whether to print relevant information in console as the function runs,
        defaults to ``False``
    :type verbose: bool
    :param pandoc_exe: absolute path to 'pandoc.exe', defaults to ``None``
        (on Windows, use the default installation path - ``"C:\\Program Files\\Pandoc\\pandoc.exe"``)
    :type pandoc_exe: str or None
    :param kwargs: [optional] parameters of `pypandoc.convert_file <https://github.com/bebraw/pypandoc>`_

    **Example**::

        >>> from pyhelpers.text import convert_md_to_rst
        >>> from pyhelpers.dir import cd

        >>> dat_dir = cd("tests\\documents")

        >>> path_to_md_file = cd(dat_dir, "readme.md")
        >>> path_to_rst_file = cd(dat_dir, "readme.rst")

        >>> convert_md_to_rst(path_to_md_file, path_to_rst_file, verbose=True)
        Converting "tests\\data\\markdown.md" to "tests\\data\\markdown.rst" ... Done.
    """

    abs_md_path, abs_rst_path = pathlib.Path(path_to_md), pathlib.Path(path_to_rst)
    # assert abs_md_path.suffix == ".md" and abs_rst_path.suffix == ".rst"

    if verbose:
        rel_md_path, rel_rst_path = map(
            lambda x: pathlib.Path(os.path.relpath(x)), (abs_md_path, abs_rst_path))

        if not os.path.exists(abs_rst_path):
            msg = "Converting \"{}\" to \"{}\"".format(rel_md_path, rel_rst_path)
        else:
            msg = "Updating \"{}\" at \"{}\\\"".format(rel_rst_path.name, rel_rst_path.parent)
        print(msg, end=" ... ")

    pandoc_exe_ = copy.copy(pandoc_exe)
    if pandoc_exe_ is None:
        pandoc_exe_ = find_executable(
            app_name="pandoc.exe", possibilities=["C:\\Program Files\\Pandoc\\pandoc.exe"])

    try:
        subprocess.call(
            '"{}" "{}" -f markdown -t rst -s -o "{}"'.format(pandoc_exe_, abs_md_path, abs_rst_path))

        if verbose:
            print("Done.")

    except FileNotFoundError:
        import pypandoc

        pypandoc.convert_file(str(abs_md_path), 'rst', outputfile=str(abs_rst_path), **kwargs)

        if verbose:
            print("Done.")

    except Exception as e:
        print("Failed. {}".format(e))
