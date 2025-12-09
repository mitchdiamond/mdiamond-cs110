# Copyright 2020, Brigham Young University-Idaho. All rights reserved.
import tkinter
from flashcards import FlashcardApp
from pytest import approx
import pytest


ENGLISH_INDEX = 0
KANJI_INDEX = 1


def test_load_card_bank():
    filename = "110-05-Functions\\FinalProject\\word_list.csv"

    root = tkinter.Tk()
    root.option_add("*font", "Helvetica 32")

    temp_flash_card_app = FlashcardApp(root)


    japanese_dictionary = temp_flash_card_app.load_card_bank(filename)

    # Verify that the make_periodic_table function returns a dictionary.
    assert isinstance(japanese_dictionary, dict), \
        "make_periodic_table function must return a dictionary: " \
        f" expected a dictionary but found a {type(japanese_dictionary)}"

    check_word(japanese_dictionary,"行く", ["Go","行く"])
    check_word(japanese_dictionary,"見る", ["See","見る"])
    check_word(japanese_dictionary,"多い", ["Many","多い"])
    check_word(japanese_dictionary,"家", ["Home","家"])
    check_word(japanese_dictionary,"これ", ["This","これ"])
    check_word(japanese_dictionary,"それ", ["That","それ"])
    check_word(japanese_dictionary,"私", ["I","私"])
    check_word(japanese_dictionary,"仕事", ["Work","仕事"])
    check_word(japanese_dictionary,"いつ", ["When","いつ"])
    check_word(japanese_dictionary,"する", ["Do","する"])
    check_word(japanese_dictionary,"出る", ["Leave","出る"])
    check_word(japanese_dictionary,"使う", ["Use","使う"])
    check_word(japanese_dictionary,"所", ["Place","所"])
    check_word(japanese_dictionary,"作る", ["Make","作る"])
    check_word(japanese_dictionary,"思う", ["Think","思う"])
    check_word(japanese_dictionary,"持つ", ["Have","持つ"])
    check_word(japanese_dictionary,"買う", ["Buy","買う"])
    check_word(japanese_dictionary,"時間", ["Time","時間"])
    check_word(japanese_dictionary,"知る", ["Know","知る"])
    check_word(japanese_dictionary,"同じ", ["Same","同じ"])
    check_word(japanese_dictionary,"今", ["Now","今"])
    check_word(japanese_dictionary,"新しい", ["New","新しい"])
    check_word(japanese_dictionary,"なる", ["Become","なる"])
    check_word(japanese_dictionary,"まだ", ["Yet","まだ"])
    check_word(japanese_dictionary,"あと", ["After","あと"])
    check_word(japanese_dictionary,"聞く", ["Hear","聞く"])
    check_word(japanese_dictionary,"言う", ["Say","言う"])
    check_word(japanese_dictionary,"少ない", ["Few","少ない"])
    check_word(japanese_dictionary,"高い", ["High","高い"])
    check_word(japanese_dictionary,"子供", ["Child","子供"])
    check_word(japanese_dictionary,"そう", ["So","そう"])
    check_word(japanese_dictionary,"もう", ["Already","もう"])
    check_word(japanese_dictionary,"学生", ["Student","学生"])
    check_word(japanese_dictionary,"熱い", ["Hot","熱い"])
    check_word(japanese_dictionary,"どうぞ", ["Please","どうぞ"])
    check_word(japanese_dictionary,"午後", ["Afternoon","午後"])
    check_word(japanese_dictionary,"長い", ["Long","長い"])
    check_word(japanese_dictionary,"本", ["Book","本"])
    check_word(japanese_dictionary,"今年", ["This Year","今年"])
    check_word(japanese_dictionary,"よく", ["Often","よく"])
    check_word(japanese_dictionary,"彼女", ["She","彼女"])
    check_word(japanese_dictionary,"どう", ["How","どう"])
    check_word(japanese_dictionary,"言葉", ["Word","言葉"])
    check_word(japanese_dictionary,"顔", ["Face","顔"])
    check_word(japanese_dictionary,"終わる", ["Finish","終わる"])
    check_word(japanese_dictionary,"一つ", ["One","一つ"])
    check_word(japanese_dictionary,"あげる", ["Give","あげる"])
    check_word(japanese_dictionary,"こう", ["Such","こう"])
    check_word(japanese_dictionary,"学校", ["School","学校"])
    check_word(japanese_dictionary,"くれる", ["Be Given","くれる"])
    check_word(japanese_dictionary,"始める", ["Start","始める"])
    check_word(japanese_dictionary,"起きる", ["Get Up","起きる"])
    check_word(japanese_dictionary,"春", ["Spring","春"])
    check_word(japanese_dictionary,"午前", ["Morning","午前"])
    check_word(japanese_dictionary,"別", ["Different","別"])
    check_word(japanese_dictionary,"どこ", ["Where","どこ"])
    check_word(japanese_dictionary,"部屋", ["Room","部屋"])
    check_word(japanese_dictionary,"若い", ["Young","若い"])
    check_word(japanese_dictionary,"車", ["Car","車"])
    check_word(japanese_dictionary,"置く", ["Put","置く"])




def check_word(japanese_dictionary, kanji, expected):
    """Verify that the actual element that came from the
    periodic_table_dict contains the same values as the
    expected element.

    Parameters
        symbol: a symbol for a chemical element
        expected: a list that contains the expected values for symbol
    Return: nothing
    """
    # Verify that symbol is in the periodic table dictionary.
    assert kanji in japanese_dictionary, \
        f'"{kanji}" is missing from the periodic table dictionary.'
    actual = japanese_dictionary[kanji]

    # Verify that the element's name is correct.
    act_kanji = actual[KANJI_INDEX]
    exp_kanji = expected[KANJI_INDEX]
    assert act_kanji == exp_kanji, \
            f'wrong Kanji for "{kanji}": ' \
            f'expected {exp_kanji} but found {act_kanji}'

    # Verify that the element's atomic mass is correct.
    act_eng = actual[ENGLISH_INDEX]
    exp_eng = expected[ENGLISH_INDEX]
    assert act_eng == approx(exp_eng), \
            f"wrong English definition for {exp_eng}: " \
            f"expected {exp_eng} but found {act_eng}"



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
