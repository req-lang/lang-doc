# Sami Dahoux (c) 2026 copyright, all rights reserved

import re
from pygments.lexer import RegexLexer, bygroups, include, words
from pygments.token import *


class ReqLexer(RegexLexer):

    name = 'Req'
    aliases = ['req']
    filenames = ['*.req']

    # Simple identifier patterns
    WORD = r'[a-zA-Z_][a-zA-Z0-9_]+'
    IDENT = r'[a-zA-Z_][a-zA-Z0-9_]*(?:::[a-zA-Z_][a-zA-Z0-9_]*)*'

    tokens = {
        'root': [
            # Whitespace
            (r'\s+', Whitespace),

            # Comments (metadata)
            (r'@@', Comment.Multiline, 'comment'),

            # Tags
            (r'#', Punctuation, 'tag'),

            # Keywords (must come before identifiers)
            (r'\bpackage\b', Keyword, 'package'),
            (r'\bpart\b', Keyword, 'part'),
            (r'\blet\b', Keyword, 'attribute'),
            (r'\brequirement\b', Keyword, 'requirement'),
            (r'\bimport\b', Keyword, 'import'),

            # Identifiers (after keywords)
            (IDENT, Name),
        ],

        'comment': [
            # Reference links {identifier}
            (r'\{', Punctuation, 'comment-link'),
            (r'[^@{]+', Comment.Multiline),
            (r'@@', Comment.Multiline, '#pop'),
            (r'@', Comment.Multiline),
        ],

        'comment-link': [
            (IDENT, Name.Variable),
            (r'\}', Punctuation, '#pop'),
            (r'\s+', Whitespace),
        ],

        'tag': [
            (r'[^\n#]+', String),
            (r'#', Punctuation, '#pop'),
            (r'\n', Whitespace, '#pop'),
        ],

        'package': [
            # Whitespace
            (r'\s+', Whitespace),

            # Comments and tags (meta)
            (r'@@', Comment.Multiline, 'comment'),
            (r'#', Punctuation, 'tag'),



            # Package end (before nested keywords)
            (r'\bpackage\n', Keyword, '#pop'),

            # Nested structures
            (r'\bpackage\b[^\S\n]+', Keyword, 'package'),
            (r'\bpart\b', Keyword, 'part'),
            (r'\brequirement\b', Keyword, 'requirement'),
            (r'\bimport\b', Keyword, 'import'),

            # Label (package name)
            (WORD, Name.Class),

            # Any other content
            (r'.', Text),
        ],

        'part': [
            # Whitespace
            (r'\s+', Whitespace),

            # Comments and tags (meta)
            (r'@@', Comment.Multiline, 'comment'),
            (r'#', Punctuation, 'tag'),

            # Part end (closing) - matches 'part' NOT followed by a name (negative lookahead)
            (r'\bpart\n', Keyword, '#pop'),
            # Nested structures
            (r'\bpart\b[^\S\n]+', Keyword, 'part'),
            (r'\blet\b', Keyword, 'attribute'),
            (r'\bimport\b', Keyword, 'import'),

            # Label (part name)
            (WORD, Name.Class),

            # Any other content
            (r'.', Text),
        ],

        'attribute': [
            # Whitespace
            (r'\s+', Whitespace),

            # Comments and tags (meta)
            (r'@@', Comment.Multiline, 'comment'),
            (r'#', Punctuation, 'tag'),

            # 'in' keyword transitions to domain
            (r'\bin\b', Keyword, 'domain'),

            # Label (attribute name)
            (WORD, Name.Attribute),

            # Any other content
            (r'.', Text),
        ],

        'domain': [
            # Whitespace
            (r'\s+', Whitespace),

            # Unit syntax
            (r'\[', Punctuation, 'unit'),

            # End of attribute (lookahead for next statement)
            (r'(?=\bpackage\b|\bpart\b|\blet\b|\brequirement\b|\bimport\b)', Text, ('#pop', '#pop')),

            # Expression content
            include('expr'),
        ],

        'unit': [
            (r'[^\]]+', String.Interpol),
            (r'\]', Punctuation, ('#pop', '#pop', '#pop')),
        ],

        # Expression states
        'expr': [
            # String literals
            (r"'([^'\\]|\\.)*'", String.Single),

            # Expression keywords (before identifiers)
            (words((
                'if', 'then', 'else', 'end', 'when', 'case', 'otherwise',
                'forall', 'exists', 'select', 'such', 'that',
                'minimize', 'maximize', 'all', 'any',
                'previously', 'rising', 'falling', 'eventually', 'always'
            ), suffix=r'\b'), Keyword),

            # Operator keywords
            (words((
                'and', 'or', 'xor', 'not', 'implies', 'iff',
                'union', 'intersection', 'difference', 'complement', 'includes',
                'since', 'in'
            ), suffix=r'\b'), Operator.Word),

            # Literals
            (words(('true', 'false', 'undefined', 'infinity'), suffix=r'\b'), Name.Builtin),

            # Numbers
            include('number'),

            # Comparison and arithmetic operators
            (r'>=|<=|/=|=|>|<', Operator),
            (r'\+|-|\*|/|%|\^', Operator),
            (r'!', Operator),

            # Punctuation
            (r'\{', Punctuation, 'set'),
            (r'\(', Punctuation),
            (r'\)', Punctuation),
            (r',', Punctuation),

            # Identifiers (with :: support)
            (IDENT, Name.Variable),
        ],

        'number': [
            # Real numbers with scientific notation
            (r'[0-9]+\.[0-9]*(?:[eE][+-]?[0-9]+)?', Number.Float),
            # Scientific notation without decimal
            (r'[0-9]+[eE][+-]?[0-9]+', Number.Float),
            # Integers
            (r'[0-9]+', Number.Integer),
        ],

        'set': [
            # Whitespace
            (r'\s+', Whitespace),
            # Set contents (expressions)
            include('expr'),
            (r'\}', Punctuation, '#pop'),
        ],

        'requirement': [
            # Whitespace
            (r'\s+', Whitespace),

            # Comments and tags (meta)
            (r'@@', Comment.Multiline, 'comment'),
            (r'#', Punctuation, 'tag'),

            # Requirement end (before other keywords)
            (r'\brequirement\b', Keyword, '#pop'),

            # 'is' keyword transitions to inner
            (r'\bis\b', Keyword, 'inner'),

            # Traceability keywords
            (r'\brefines\b', Keyword),
            (r'\bspecializes\b', Keyword),
            (r'\bderives\b', Keyword),

            # Identifiers (for name or traceability target)
            (IDENT, Name.Function),

            # Any other content
            (r'.', Text),

        ],

        'inner': [
            # Whitespace
            (r'\s+', Whitespace),

            # Comments (inner content with links)
            (r'@@', Comment.Multiline, 'comment'),

            # Requirement end
            (r'\brequirement\b', Keyword, ('#pop', '#pop')),

            # Expression content (for formal requirements)
            include('expr'),
        ],

        'import': [
            # Whitespace
            (r'\s+', Whitespace),

            # Identifier (module to import)
            (IDENT, Name.Namespace, '#pop'),
        ],
    }
