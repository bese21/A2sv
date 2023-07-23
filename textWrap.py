import textwrap

def wrap(string, max_width):
    txt=""
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(text=string)
    for line in word_list:
        txt=txt+line+"\n"
        
    return txt

    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
