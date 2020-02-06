"""
Slicing string

Expected Result:

*** test words slicing : 0123456789
 1. words[-1]    : result:9         , expected:9         , assert:True
 2. words[-2]    : result:8         , expected:8         , assert:True
 3. words[2:8]   : result:234567    , expected:234567    , assert:True
 4. words[-2:]   : result:89        , expected:89        , assert:True
 5. words[-1:]   : result:9         , expected:9         , assert:True
 6. words[:-2]   : result:01234567  , expected:01234567  , assert:True
 7. words[-0]    : result:0         , expected:0         , assert:True
 8. words[0:9:2] : result:02468     , expected:02468     , assert:True
 9. words[::-2]  : result:97531     , expected:97531     , assert:True
10. words[2:8:-2]: result:          , expected:          , assert:True

"""


def test_slicing():
    words = "0123456789"

    print(f"\n*** test words slicing : {words}")
    test_cases = [
        {"title": "words[-1]    ", "words": words[-1]    , "expected": "9"         },
        {"title": "words[-2]    ", "words": words[-2]    , "expected": "8"         },
        {"title": "words[2:8]   ", "words": words[2:8]   , "expected": "234567"    },
        {"title": "words[-2:]   ", "words": words[-2:]   , "expected": "89"        },
        {"title": "words[-1:]   ", "words": words[-1:]   , "expected": "9"         },
        {"title": "words[:-2]   ", "words": words[:-2]   , "expected": "01234567"  },
        {"title": "words[-0]    ", "words": words[-0]    , "expected": "0"         },
        {"title": "words[0:9:2] ", "words": words[0:9:2] , "expected": "02468"     },
        {"title": "words[::-2]  ", "words": words[::-2]  , "expected": "97531"     },
        {"title": "words[2:8:-2]", "words": words[2:8:-2], "expected": ""          } 
    ]

    for i, test_case in enumerate(test_cases, 1):
        t = test_case['title']
        w = test_case['words']
        e = test_case['expected']
        a = w == e
        print(f"{i:2}. {t}: result:{w:10}, expected:{e:10}, assert:{a}") 


if __name__ == '__main__':
    test_slicing()

