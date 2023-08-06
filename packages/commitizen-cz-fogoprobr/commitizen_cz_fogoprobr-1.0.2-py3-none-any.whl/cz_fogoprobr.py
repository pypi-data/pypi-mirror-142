from commitizen.cz.base import BaseCommitizen
from commitizen.cz.utils import multiple_line_breaker, required_validator

def parse_scope(text):
    if not text:
        return ""

    scope = text.strip().split()
    if len(scope) == 1:
        return scope[0]

    return "-".join(scope)

def parse_subject(text):
    if isinstance(text, str):
        text = text.strip(".").strip()

    return required_validator(text, msg="Assunto é obrigatório.")

class FogoprobrCz(BaseCommitizen):
    def questions(self) -> list:
        """Perguntas sobre a mensagem de commit.

        Deve seguir o formato 'whaaaaat'.
        Mais Sobre: https://github.com/finklabs/whaaaaat/

        :rtype: list
        """
        questions = [
            {
                "type": "list",
                "name": "prefix",
                "message": "Selecione o tipo de alteração que você está 'commitando'",
                "choices": [
                    {
                        "value": "fix",
                        "name": "fix: Concerta bug",
                        "key": "x",
                    },
                    {
                        "value": "feat",
                        "name": "feat: Implementa ou adiciona feature",
                        "key": "f",
                    },
                    {
                        "value": "doc",
                        "name": "doc: Mudanças apenas de documentação",
                        "key": "d",
                    },
                    {
                        "value": "chore",
                        "name": (
                            "chore: Alterações que não afetam o "
                            "sentido do código (white-space, formatação,"
                            " semi-colons, criação file/folder)"
                        ),
                        "key": "c",
                    },
                    {
                        "value": "refactor",
                        "name": (
                            "refactor: Alterações de código que não concerta "
                            "um bug e nem adiciona feature"
                        ),
                        "key": "r",
                    },
                    {
                        "value": "perf",
                        "name": "perf: Mudanças de código que melhoram performance",
                        "key": "p",
                    },
                    {
                        "value": "test",
                        "name": (
                            "test: Adição ou correção de " "testes existentes"
                        ),
                        "key": "t",
                    },
                ],
            },
            {
                "type": "input",
                "name": "scope",
                "message": (
                    "Qual é o escopo da mudança? (class ou file name): ( [enter]  para pular )\n"
                ),
                "filter": parse_scope,
            },
            {
                "type": "input",
                "name": "subject",
                "filter": parse_subject,
                "message": (
                    "Escreva um breve resumo imperativo das alterações do código: ( lower case e sem pontuação )\n"
                ),
            },
            {
                "type": "input",
                "name": "body",
                "message": (
                    "Forneça informações adicionais sobre o contexto das alterações de código: ( [enter] para pular )\n"
                ),
                "filter": multiple_line_breaker,
            },
        ]
        return questions

    def message(self, answers: dict) -> str:
        """Gera a mensagem com as respostas dadas.

        :type answers: dict
        :rtype: string
        """
        prefix = answers["prefix"]
        scope = answers["scope"]
        subject = answers["subject"]
        body = answers["body"]

        if scope:
            scope = f"({scope})"
        if body:
            body = f"\n\n{body}"

        message = f"{prefix}{scope}: {subject}{body}"

        return message

    def example(self):
        """Forneça um exemplo para ajudar a entender o estilo [OPCIONAL]
        Usado pelo exemplo cz.

        :rtype: string
        """
        return 'doc(README.md): adiciona tutorial de instalacao'

    def schema(self) -> str:
        """Mostrar o schema usado [OPCIONAL]

        :rtype: string
        """
        return (
            "<type>(<scope>): <subject>\n"
            "<BLANK LINE>\n"
            "<body>"
        )

    def info(self) -> str:
        return (
            "O commit contém os seguintes elementos estruturais, para documentar\n"
            "aos consumidores da biblioteca:\n\n"

            "fix: um commit do tipo fix corrige um bug em sua base de código\n\n"

            "feat: um commit do tipo feat introduz um novo recurso na base de código\n\n"

            "Outros: tipos de commit diferentes de fix: e feat: são permitidos,\n"
            "como doc:, chore:, refactor:, perf: e test:.\n\n"

            "Um escopo pode ser fornecido para um tipo de confirmação, para fornecer contexto informação\n"
            "adicional e está contida entre parênteses, por exemplo, feat(parser): adiciona a capacidade de analisar matrizes.\n"

            "<type>[optional scope]: <description>\n"

            "[optional body]"
        )

discover_this = FogoprobrCz