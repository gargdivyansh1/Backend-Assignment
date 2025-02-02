from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField(_("Question"))
    answer = RichTextField(_("Answer"))  # WYSIWYG Editor

    # Translations
    question_hi = models.TextField(_("Question in Hindi"), blank=True, null=True)
    question_bn = models.TextField(_("Question in Bengali"), blank=True, null=True)
    answer_hi = RichTextField(_("Answer in Hindi"), blank=True, null=True)
    answer_bn = RichTextField(_("Answer in Bengali"), blank=True, null=True)

    def get_translated(self, lang):
        """Return translated question & answer based on the selected language."""
        if lang == "hi":
            return self.question_hi or self.question, self.answer_hi or self.answer
        elif lang == "bn":
            return self.question_bn or self.question, self.answer_bn or self.answer
        return self.question, self.answer  # Default to English

    def save(self, *args, **kwargs):
        translator = Translator()
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest="hi").text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest="bn").text
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, dest="hi").text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, dest="bn").text
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
