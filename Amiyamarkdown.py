import sublime, sublime_plugin
class Akiyamarkdown(sublime_plugin.TextCommand):
    def run(self, edit):
        scope = self.view.scope_name(self.view.sel()[0].begin()-1)
        if "text.amd" in scope:
            line = self.view.line(self.view.sel()[0].begin())
            text = self.view.substr(line)
            indent = text.count('　')

            if "keyword.title" in scope:
                self.view.insert(edit, line.end(), "\n"+("　"*(indent) )+ "■")

            if "keyword.subtitle" in scope:
                self.view.insert(edit, line.end(), "\n"+("　"*(indent) )+"・")

            if "keyword.smalltitle" in scope:
                self.view.insert(edit, line.end(), "\n"+("　"*indent)+"・")

            if "keyword.indent" in scope:
                self.view.insert(edit, line.end(), "\n"+("　"*indent)+"→")

class Akiyamaspace(sublime_plugin.TextCommand):
    def run(self, edit):
        scope = self.view.scope_name(self.view.sel()[0].begin()-1)
        if "text.amd" in scope:
            parentLine = self.view.line(self.view.sel()[0].begin()-self.view.rowcol(self.view.sel()[0].begin())[1]-1)
            parentText = self.view.substr(parentLine)
            parentIndent = parentText.count('　')

            line = self.view.line(self.view.sel()[0].begin())
            text = self.view.substr(line)
            indent = text.count('　')

            if indent < parentIndent:
                self.view.insert(edit, line.begin(), ("　"*(parentIndent-indent) ))
            elif "keyword.smalltitle" in scope:
                self.view.insert(edit, line.end(), ("　") )
            else:
                self.view.insert(edit, line.begin(), ("　") )

            if self.view.find_all("・　"):
                for region in self.view.find_all('・　'):
                    self.view.replace(edit, region, '　→')


