# Regular Expressions

- Regular Expressions or RegEx is a pattern to find within the data.

## RegEx Topics

- All Tokens
- Common Tokens
- General Tokens
- Anchors
- Meta Sequences
- Quantifiers
- Group Constructs
- Character Classes
- Flags/Modifiers
- Substitution

### Validation without Regular Expressions

- How would you evaluate your email address when the user inputs it? For example, you would need to evaulate '@' sign in the email address along with their email patterns.

#### Python re library

- This Python library has functions that could be used to find patterns within the data.

#### Regular Expression Patterns

- re.search(patterns, string, flags=0)
- Patterns: . (any character except a newline)
- Patterns: * (0 or more repetitions) - 1, 2, or 300
- Patterns: + (1 or more repetitions) - At least character, 1 symbol of the same thing on the left.
- Patterns: ? (0 or 1 repetition) - Zero of this character or one.
- Patterns: {m} (m repetitions) - M repetitions, be it 1, 2, 3, or 300.
- Patterns: {m,n} (m-n repetitions) - Range of m through n repetitions.
- Patterns: ^ - Match from the start of the string.
- Patterns: $ - Match from the end of the string or just before the newline at the end of the string.
- Patterns: [] - Set of characters. Include one or more characters that you want to look for specifically.
- Patterns: [^] - Complementing the set. You cannot match any of these characters.
- Patterns: \w - Any word character.

#### Examples

- /\[\d{1,2}\/Jun\/\d{1,4}\:\d{1,2}\:\d{1,2}\:\d{1,2}.\-\d{1,4}\]
- Named Capture Group: `(?<Date>\[\d{2}\/Jun\/\d{4}\:\d{2}\:\d{2}\:\d{2}.\-\d{4}\])`
