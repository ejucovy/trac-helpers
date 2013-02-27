from trac.wiki.macros import WikiMacroBase

class CsrfTokenMacro(WikiMacroBase):
    def expand_macro(self, formatter, name, args):
        return formatter.req.form_token
