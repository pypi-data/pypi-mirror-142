import re

from spacy.language import Language
from spacy.tokens import Doc


@Language.factory("sentex", default_config={"sentence_regex": "", "ignore_regex": ""})
def create_sentex_component(
    nlp: Language, name: str, sentence_regex: str, ignore_regex: str
):
    return Sentex(nlp, sentence_regex, ignore_regex)


class Sentex:
    """
    Sentex is a spaCy pipeline component that adds spans to the list `Doc._.sentex`
    based on regular expression matches within each sentence of the document. If an
    `ignore_regex` is given, sentences matching that regular expression will be ignored.

    nlp: `Language`,
        A required argument for spacy to use this as a factory
    sentence_regex : `str`,
        A regular expression to match spans within each sentence of the document.
    ignore_regex : `str`,
        A regular expression to identify sentences that should be ignored.
    """

    def __init__(self, nlp: Language, sentence_regex: str, ignore_regex: str):
        self.sentence_regex = sentence_regex
        self.ignore_regex = ignore_regex

        if not Doc.has_extension("sentex"):
            Doc.set_extension("sentex", default=[])

    def __call__(self, doc: Doc) -> Doc:

        for sent in doc.sents:
            should_ignore = bool(re.search(self.ignore_regex, sent.text))
            if should_ignore:
                continue
            for match in re.finditer(self.sentence_regex, sent.text):
                start, end = match.span()
                span = sent.char_span(start, end)
                if span is not None:
                    doc._.sentex.append(span)
        return doc
