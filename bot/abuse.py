import re

PATTERNS = (r"(\b[сs]{1}[сsц]{0,1}[uуy](?:[ч4]{0,1}[иаakк][^ц])\w*\b)",
            r"(\b(?!пло|стра|[тл]и)(\w(?!(у|пло)))*[хx][уy](й|йа|[еeё]|и|я|ли|ю)(?!га)\w*\b)",
            r"(\b(п[oо]|[нз][аa])*[хx][eе][рp]\w*\b)",
            r"(\b[мm][уy][дd]([аa][кk]|[oо]|и)\w*\b)",
            r"(\b\w*д[рp](?:[oо][ч4]|[аa][ч4])(?!л)\w*\b)",
            r"(\b(?!(?:кило)?[тм]ет)(?!смо)[а-яa-z]*(?<!с)т[рp][аa][хx]\w*\b)",
            r"(\b[к|k][аaoо][з3z]+[eе]?ё?л\w*\b)",
            r"(\b(?!со)\w*п[еeё]р[нд](и|иc|ы|у|н|е|ы)\w*\b)",
            r"(\b\w*[бп][ссз]д\w+\b)",
            r"(\b([нnп][аa]?[оo]?[xх])\b)",
            r"(\b([аa]?[оo]?[нnпбз][аa]?[оo]?)?([cс][pр][аa][^зжбсвм])\w*\b)",
            r"(\b\w*([оo]т|вы|[рp]и|[оo]|и|[уy]){0,1}([пnрp][iиеeё]{0,1}[3zзсcs][дd])\w*\b)",
            r"(\b(вы)?у?[еeё]?би?ля[дт]?[юоo]?\w*\b)",
            r"(\b(?!вело|ски|эн)\w*[пpp][eеиi][дd][oaоаеeирp](?![цянгюсмйчв])[рp]?(?![лт])\w*\b)",
            r"(\b(?!в?[ст]{1,2}еб)(?:(?:в?[сcз3о][тяaа]?[ьъ]?|вы|п[рp][иоo]|[уy]|р[aа][з3z][ьъ]?|к[оo]н[оo])?[её]б[а-яa-z]*)|(?:[а-яa-z]*[^хлрдв][еeё]б)\b)",
            r"(\b[з3z][аaоo]л[уy]п[аaeеин]\w*\b)",)


def check_matches(matches):
    if len(matches):
        result = []
        for match in matches:
            if type(match) == tuple:
                result.append(match[0].strip())
            else:
                result.append(match.strip())
        return result
    return ()


def matfilter(text, npattern=None):
    text = text.replace("\r\n", " ")
    text = text.replace("\n", " ")

    if npattern is not None:
        result = check_matches(
            re.findall(PATTERNS[npattern], text, re.IGNORECASE | re.VERBOSE | re.UNICODE | re.DOTALL)
        )
        if len(result):
            return result
    else:
        for pattern in PATTERNS:
            result = check_matches(re.findall(pattern, text, re.IGNORECASE | re.VERBOSE | re.UNICODE | re.DOTALL))
            if len(result):
                return result

    return ()
