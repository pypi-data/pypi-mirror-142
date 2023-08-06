import pkg_resources
import random
from keyword import kwlist

from colored import bg, stylize

_MODIFIED_KWLIST = [kw.lower() for kw in kwlist] + ["print", "reset"]
_WORDLE_LENGTH = 5
_TOTAL_NUMBER_OF_GUESSES = 6
_previous_guesses = []
_current_guess_idx = 0
_generated = False

ANSWERS_PATH = pkg_resources.resource_filename("wordle", "wordle_answers.txt")
ALLOWED_PATH = pkg_resources.resource_filename("wordle", "wordle_allowed.txt")


class _Guess:
    def __init__(self, true_word: str, this_word: str) -> None:
        assert len(this_word) == _WORDLE_LENGTH
        self.this_word = this_word
        self._update(true_word)

    def _update(self, true_word: str) -> None:
        self.true_word = true_word

    def __repr__(self) -> str:
        global _current_guess_idx
        global _previous_guesses
        tail = ""
        if self.this_word == self.true_word:
            tail = f"You got it in {_current_guess_idx + 1} guesses."
        elif _current_guess_idx + 1 == _TOTAL_NUMBER_OF_GUESSES:
            tail = f"The word was {self.true_word}."
        ls = []
        for this_letter, true_letter in zip(self.this_word, self.true_word):
            l = this_letter
            if this_letter == true_letter:
                l = stylize(this_letter, bg("green_4"))
            elif this_letter in self.true_word:
                l = stylize(this_letter, bg("gold_3b"))
            ls.append(l)
        styled_word = " ".join(ls)
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
    global _generated
    selected_answer = "error"
    with open(ANSWERS_PATH, "r") as f1:
        words = [w for w in f1.read().splitlines() if not w in _MODIFIED_KWLIST]
        selected_answer = random.choice(words)

        with open(ALLOWED_PATH, "r") as f2:
            words += [w for w in f2.read().splitlines() if not w in _MODIFIED_KWLIST]
            nops = 0
            for word in words:
                casings = [word.lower(), word.upper(), word.capitalize()]
                for case in casings:
                    try:
                        if _generated:
                            exec(
                                f"{case}._update('{selected_answer}')",
                                globals(),
                            )
                        else:
                            exec(
                                f"{case} = _Guess('{selected_answer}', '{word.lower()}')",
                                globals(),
                            )
                        nops += 1
                    except:
                        ...
            _generated = True


wordle = _Reset()
