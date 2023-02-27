
import genanki
from cached_property import cached_property
import re
import os


class ModelX(genanki.Model):
    def __init__(self, model_id=None, name=None, fields=None, templates=None, css='', type=0):
        super().__init__(model_id, name, fields, templates, css)
        self._type = type

    def to_json(self, now_ts, deck_id):
        j = super().to_json(now_ts, deck_id)
        j["type"] = self._type
        return j


class NoteX(genanki.Note):
    def _cloze_cards(self):
        """
        returns a Card with unique ord for each unique cloze reference
        """
        card_ords = set()
        # find cloze replacements in first template's qfmt, e.g "{{cloze::Text}}"
        cloze_replacements = set(re.findall("{{[^}]*?cloze:(?:[^}]?:)*(.+?)}}", self.model.templates[0]['qfmt']) +
                                 re.findall("<%cloze:(.+?)%>", self.model.templates[0]['qfmt']))
        for field_name in cloze_replacements:
          field_index = next((i for i, f in enumerate(self.model.fields) if f['name'] == field_name), -1)
          field_value = self.fields[field_index] if field_index >= 0 else ""
          # update card_ords with each cloze reference N, e.g. "{{cN::...}}"
          card_ords.update([int(m)-1 for m in re.findall("{{c(\d+)::.+?}}", field_value) if int(m) > 0])

        if card_ords == {}:
            card_ords = {0}

        return([genanki.Card(ord) for ord in card_ords])

    @cached_property
    def cards(self):
        if self.model._type == 1:
            return self._cloze_cards()
        else:
            return super().cards

