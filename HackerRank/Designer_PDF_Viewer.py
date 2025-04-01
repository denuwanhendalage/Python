def designerPdfViewer(h, word):
    word_list = list(word)
    max_element = 0
    for element in word_list:
        if h[ord(element)-97] > max_element:
            max_element = h[ord(element)-97]
    area = len(word_list) * max_element
    return area
    # Write your code here


print(designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5,
      5, 5, 5, 5, 5, 5, 5, 5, 5, 5], "abc"))  # Expected output: [1,2,3,4,5]


print(ord('b'))
print(list('abc'))
