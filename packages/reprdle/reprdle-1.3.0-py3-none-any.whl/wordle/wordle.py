from collections import defaultdict
import pkg_resources
import random
from keyword import kwlist
from colored import bg, stylize

_MODIFIED_KWLIST = [kw.lower() for kw in kwlist] + ["print", "reset"]
_WORDLE_LENGTH = 5
_TOTAL_NUMBER_OF_GUESSES = 6
_previous_guesses = []
_current_guess_idx = 0
ANSWERS_PATH = pkg_resources.resource_filename("wordle", "wordle_answers.txt")
ALLOWED_PATH = pkg_resources.resource_filename("wordle", "wordle_allowed.txt")


class _Guess:
    def __init__(self, true_word: str, this_word: str) -> None:
        assert len(this_word) == _WORDLE_LENGTH
        self.this_word = this_word
        self.true_word = true_word

    def __repr__(self) -> str:
        global _current_guess_idx
        tail = ""
        if self.this_word == self.true_word:
            tail = f"You got it in {_current_guess_idx + 1} guesses."
        elif _current_guess_idx + 1 == _TOTAL_NUMBER_OF_GUESSES:
            tail = f"The word was {self.true_word}."
        ls = []
        n_matched = defaultdict(lambda: 0)
        for this_letter, true_letter in zip(self.this_word, self.true_word):
            l = this_letter
            if this_letter == true_letter:
                l = stylize(this_letter, bg("green_4"))
                n_matched[this_letter] += 1
            elif this_letter in self.true_word and n_matched[
                this_letter
            ] < self.true_word.count(this_letter):
                l = stylize(this_letter, bg("gold_3b"))
                n_matched[this_letter] += 1
            ls.append(l)
        styled_word = " ".join(ls)
        if styled_word in _previous_guesses:
            return "\n".join(_previous_guesses) + "\nAlready guessed."
        _previous_guesses[_current_guess_idx] = styled_word
        out = "\n".join(_previous_guesses) + "\n" + tail
        _current_guess_idx += 1
        if tail != "":
            _reset()
        return out


class _Reset:
    def __init__(self) -> None:
        _reset()

    def __repr__(self) -> str:
        _reset()
        return ""


def _reset():
    global _previous_guesses
    _previous_guesses = ["# " * _WORDLE_LENGTH] * _TOTAL_NUMBER_OF_GUESSES
    global _current_guess_idx
    _current_guess_idx = 0
    selected_answer = "error"
    with open(ANSWERS_PATH, "r") as f1:
        words = [w for w in f1.read().splitlines() if not w in _MODIFIED_KWLIST]
        selected_answer = random.choice(words)
        with open(ALLOWED_PATH, "r") as f2:
            words += [w for w in f2.read().splitlines() if not w in _MODIFIED_KWLIST]
            for word in words:
                casings = [word.lower(), word.upper(), word.capitalize()]
                for case in casings:
                    try:
                        globals()[case] = _Guess(selected_answer, word.lower())
                    except:
                        ...


wordle = _Reset()
