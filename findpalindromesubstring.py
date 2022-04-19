from collections import Counter

def search(pat, txt):

    txt_len = len(txt)
    pattern_len = len(pat)
    pattern_count = Counter(pat)

    for i in range(0, txt_len - pattern_len + 1):
        text_count = Counter(txt[i:i+pattern_len])

        if pattern_count == text_count:
            print("Found at Index {}".format(i))

                         
txt = "BACDGABCDA"
pat = "ABCD"      
search(pat, txt)  
