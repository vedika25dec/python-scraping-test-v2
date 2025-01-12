

## TASK 1 TEST 
import pytest
from src import longest_sequence,is_grandma_list  # Import your function

def test_longest_sequence_basic():
    keywords = ['milk', 'catalog', 'c+', 'python', 'cat','dog1','dog2','dog3','python2','python5','pyth','dataman','datamanger','dataanalyst']
    result = longest_sequence(keywords)
    assert result == 'pyth'  


def test_longest_sequence_with_duplicates():
    keywords = ['aab', 'abb', 'ab']
    result = longest_sequence(keywords)
    assert result == 'ab'  # 



## IN CMD RUN: pytest test_src.py

# Individual Code

# TASK 3 TEST

def test_grandma1():
    SUBLIST = [1, 2, [[4, 5], [4, 7]], 5, 4, [[95], [2]]]
    result = is_grandma_list(SUBLIST)
    assert result == True  


def test_grandma2():
    SUBLIST = [5, 9, 4, [[8, 7]], 4, 7, [[5]]]
    result = is_grandma_list(SUBLIST)
    assert result == False  # 


## IN CMD RUN: pytest test_src.py