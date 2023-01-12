import operator


def Word_Order_Frequency_One_Book(Book, Word_Order, File_Output):
    if Word_Order==1:
        try:        #if file path exist
             file = open(Book, "r", encoding="utf-8")
             word = file.read()         #reading txt file
             words = word.split(' ')    #spliting word
             stop_words = ['able', 'about', 'above', 'abroad', "\n", 'according', "", 'accordingly',
                           'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against',
                           'ago', 'ahead', 'aint', 'all', 'allow', 'allows', 'almost', 'alone',
                           'along', 'alongside', 'already', 'also', 'although', 'always', 'am',
                           'amid', 'amidst', 'among', 'amongst', 'an', 'and', 'another', 'any',
                           'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways',
                           'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are',
                           'arent', 'around', 'as', 'as', 'aside', 'ask', 'asking', 'associated',
                           'at', 'available', 'away', 'awfully', 'back', 'backward', 'backwards',
                           'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been',
                           'before', 'beforehand', 'begin', 'behind', 'being', 'believe', 'below',
                           'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both',
                           'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', 'cant',
                           'caption', 'cause', 'causes', 'certain', 'certainly', 'changes',
                           'clearly', 'cmon', 'co', 'co', 'com', 'come', 'comes', 'concerning',
                           'consequently', 'consider', 'considering', 'contain', 'containing',
                           'contains', 'corresponding', 'could', 'couldnt', 'course', 'cs',
                           'currently', 'dare', 'darent', 'definitely', 'described', 'despite',
                           'did', 'didnt', 'different', 'directly', 'do', 'does', 'doesnt',
                           'doing', 'done', 'dont', 'down', 'downwards', 'during', 'each', 'edu',
                           'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end',
                           'ending', 'enough', 'entirely', 'especially', 'et', 'etc', 'even',
                           'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything',
                           'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far',
                           'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed',
                           'following', 'follows', 'for', 'forever', 'former', 'formerly',
                           'forth', 'forward', 'found', 'four', 'from', 'further', 'furthermore',
                           'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going',
                           'gone', 'got', 'gotten', 'greetings', 'had', 'hadnt', 'half',
                           'happens', 'hardly', 'has', 'hasnt', 'have', 'havent', 'having', 'he',
                           'hed', 'hell', 'hello', 'help', 'hence', 'her', 'here', 'hereafter',
                           'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes',
                           'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit',
                           'however', 'hundred', 'id', 'ie', 'if', 'ignored', 'ill', 'im',
                           'immediate', 'in', 'inasmuch', 'inc', 'inc', 'indeed', 'indicate',
                           'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead',
                           'into', 'inward', 'is', 'isnt', 'it', 'itd', 'itll', 'its', 'its',
                           'itself', 'ive', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'known',
                           'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least',
                           'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'likewise',
                           'little', 'look', 'looking', 'looks', 'low', 'lower', 'ltd', 'made',
                           'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'maynt', 'me',
                           'mean', 'meantime', 'meanwhile', 'merely', 'might', 'mightnt', 'mine',
                           'minus', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs',
                           'much', 'must', 'mustnt', 'my', 'myself', 'name', 'namely', 'nd',
                           'near', 'nearly', 'necessary', 'need', 'neednt', 'needs', 'neither',
                           'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine',
                           'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone',
                           'noone', 'nor', 'normally', 'not', 'nothing', 'notwithstanding',
                           'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh',
                           'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'ones', 'only',
                           'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought',
                           'oughtnt', 'our', 'ours', 'ourselves', 'out', 'outside', 'over',
                           'overall', 'own', 'particular', 'particularly', 'past', 'per',
                           'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably',
                           'probably', 'provided', 'provides', 'que', 'quite', 'qv', 'rather',
                           'rd', 're', 'really', 'reasonably', 'recent', 'recently', 'regarding',
                           'regardless', 'regards', 'relatively', 'respectively', 'right',
                           'round', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second',
                           'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems',
                           'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously',
                           'seven', 'several', 'shall', 'shant', 'she', 'shed', 'shell', 'shes',
                           'should', 'shouldnt', 'since', 'six', 'so', 'some', 'somebody', 'someday',
                           'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat',
                           'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying',
                           'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'taking',
                           'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that',
                           'thatll', 'thats', 'thats', 'thatve', 'the', 'their', 'theirs', 'them',
                           'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby',
                           'thered', 'therefore', 'therein', 'therell', 'therere', 'theres',
                           'theres', 'thereupon', 'thereve', 'these', 'they', 'theyd', 'theyll',
                           'theyre', 'theyve', 'thing', 'things', 'think', 'third', 'thirty',
                           'this', 'thorough', 'thoroughly', 'those', 'though', 'three',
                           'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together',
                           'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try',
                           'trying', 'ts', 'twice', 'two', 'un', 'under', 'underneath', 'undoing',
                           'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up',
                           'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using',
                           'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz',
                           'vs', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome',
                           'well', 'well', 'went', 'were', 'were', 'werent', 'weve', 'what',
                           'whatever', 'whatll', 'whats', 'whatve', 'when', 'whence', 'whenever',
                           'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres',
                           'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while',
                           'whilst', 'whither', 'who', 'whod', 'whoever', 'whole', 'wholl',
                           'whom', 'whomever', 'whos', 'whose', 'why', 'will', 'willing', 'wish',
                           'with', 'within', 'without', 'wonder', 'wont', 'would', 'wouldnt',
                           'yes', 'yet', 'you', 'youd', 'youll', 'your', 'youre', 'yours',
                           'yourself', 'yourselves', 'youve', 'zero', 'a', 'hows', 'i', 'whens',
                           'whys', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o',
                           'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'i', 'www',
                           'amount', 'bill', 'bottom', 'call', 'computer', 'con', 'couldnt',
                           'cry', 'de', 'describe', 'detail', 'due', 'eleven', 'empty', 'fifteen',
                           'fifty', 'fill', 'find', 'fire', 'forty', 'front', 'full', 'give',
                           'hasnt', 'herse', 'himse', 'interest', 'itse', 'mill', 'move', 'myse',
                           'part', 'put', 'show', 'side', 'sincere', 'sixty', 'system', 'ten',
                           'thick', 'thin', 'top', 'twelve', 'twenty', 'abst', 'accordance',
                           'act', 'added', 'adopted', 'affected', 'affecting', 'affects', 'ah',
                           'announce', 'anymore', 'apparently', 'approximately', 'aren', 'arent',
                           'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol',
                           'briefly', 'ca', 'date', 'ed', 'effect', 'etal', 'ff', 'fix', 'gave',
                           'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im', 'immediately',
                           'importance', 'important', 'index', 'information', 'invention', 'itd',
                           'keys', 'kg', 'km', 'largely', 'lets', 'line', 'll', 'means', 'mg',
                           'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted',
                           'obtain', 'obtained', 'omitted', 'ord', 'owing', 'page', 'pages',
                           'poorly', 'possibly', 'potentially', 'pp', 'predominantly', 'present',
                           'previously', 'primarily', 'promptly', 'proud', 'quickly', 'ran',
                           'readily', 'ref', 'refs', 'related', 'research', 'resulted',
                           'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes',
                           'showed', 'shown', 'showns', 'shows', 'significant', 'significantly',
                           'similar', 'similarly', 'slightly', 'somethan', 'specifically',
                           'state', 'states', 'stop', 'strongly', 'substantially', 'successfully',
                           'sufficiently', 'suggest', 'thered', 'thereof', 'therere', 'thereto',
                           'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til',
                           'tip', 'ts', 'ups', 'usefully', 'usefulness', 've', 'vol', 'vols',
                           'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words',
                           'world', 'youd', 'youre']
             
             
            
             dictionary_word = {}
             punc = '''!()-'"[]" 0123456789"{};:"\,’<“>""./?@#$%^&*_~'''

             for i in words:                                  
                 i = i.lower()
                 i=i.replace("\n","")
                 for ele in i:            #removing punctuation
                     if ele in punc:
                         i = i.replace(ele, "")
                 if i in dictionary_word and i not in stop_words:                              # removing stop words
                     dictionary_word[i] += 1                          #If it's in it, the key is incremented by one.
                 elif i not in stop_words:                            #otherwise add it in     
                     dictionary_word[i] = 1
             sorted_words = {}
             sorted_words = sorted(dictionary_word.items(), key=lambda x: x[1], reverse=True)  # sorting words
             file_for_write = open(File_Output, "w")                                           #writing output to txt file
             file_for_write.write("| WORD       | WORD     |\n"   #Writing txt file operations
                   "| ORDER      | ORDER    |\n"
                   "| FREQUENCY  | SEQUENCE |\n")
             file_for_write.close()
             file_append=open(File_Output, "a")
             for i in range(100):
                 file_append.write("{:7}          {:15}\n".format(sorted_words[i][1], sorted_words[i][0]))
                 
             file_append.close()
        except :#throw file not found exception
             print("File not Found!")
        
       
         
        
       
        
        
    elif Word_Order==2:      
        try:#try catch file path does not exist throws file not found exception
            file = open(Book, "r", encoding="utf-8")
            word1 = file.read()
            stop_words = ['able', 'about', 'above', 'abroad', "\n", 'according', "", 'accordingly',
                           'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against',
                           'ago', 'ahead', 'aint', 'all', 'allow', 'allows', 'almost', 'alone',
                           'along', 'alongside', 'already', 'also', 'although', 'always', 'am',
                           'amid', 'amidst', 'among', 'amongst', 'an', 'and', 'another', 'any',
                           'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways',
                           'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are',
                           'arent', 'around', 'as', 'as', 'aside', 'ask', 'asking', 'associated',
                           'at', 'available', 'away', 'awfully', 'back', 'backward', 'backwards',
                           'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been',
                           'before', 'beforehand', 'begin', 'behind', 'being', 'believe', 'below',
                           'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both',
                           'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', 'cant',
                           'caption', 'cause', 'causes', 'certain', 'certainly', 'changes',
                           'clearly', 'cmon', 'co', 'co', 'com', 'come', 'comes', 'concerning',
                           'consequently', 'consider', 'considering', 'contain', 'containing',
                           'contains', 'corresponding', 'could', 'couldnt', 'course', 'cs',
                           'currently', 'dare', 'darent', 'definitely', 'described', 'despite',
                           'did', 'didnt', 'different', 'directly', 'do', 'does', 'doesnt',
                           'doing', 'done', 'dont', 'down', 'downwards', 'during', 'each', 'edu',
                           'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end',
                           'ending', 'enough', 'entirely', 'especially', 'et', 'etc', 'even',
                           'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything',
                           'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far',
                           'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed',
                           'following', 'follows', 'for', 'forever', 'former', 'formerly',
                           'forth', 'forward', 'found', 'four', 'from', 'further', 'furthermore',
                           'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going',
                           'gone', 'got', 'gotten', 'greetings', 'had', 'hadnt', 'half',
                           'happens', 'hardly', 'has', 'hasnt', 'have', 'havent', 'having', 'he',
                           'hed', 'hell', 'hello', 'help', 'hence', 'her', 'here', 'hereafter',
                           'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes',
                           'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit',
                           'however', 'hundred', 'id', 'ie', 'if', 'ignored', 'ill', 'im',
                           'immediate', 'in', 'inasmuch', 'inc', 'inc', 'indeed', 'indicate',
                           'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead',
                           'into', 'inward', 'is', 'isnt', 'it', 'itd', 'itll', 'its', 'its',
                           'itself', 'ive', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'known',
                           'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least',
                           'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'likewise',
                           'little', 'look', 'looking', 'looks', 'low', 'lower', 'ltd', 'made',
                           'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'maynt', 'me',
                           'mean', 'meantime', 'meanwhile', 'merely', 'might', 'mightnt', 'mine',
                           'minus', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs',
                           'much', 'must', 'mustnt', 'my', 'myself', 'name', 'namely', 'nd',
                           'near', 'nearly', 'necessary', 'need', 'neednt', 'needs', 'neither',
                           'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine',
                           'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone',
                           'noone', 'nor', 'normally', 'not', 'nothing', 'notwithstanding',
                           'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh',
                           'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'ones', 'only',
                           'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought',
                           'oughtnt', 'our', 'ours', 'ourselves', 'out', 'outside', 'over',
                           'overall', 'own', 'particular', 'particularly', 'past', 'per',
                           'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably',
                           'probably', 'provided', 'provides', 'que', 'quite', 'qv', 'rather',
                           'rd', 're', 'really', 'reasonably', 'recent', 'recently', 'regarding',
                           'regardless', 'regards', 'relatively', 'respectively', 'right',
                           'round', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second',
                           'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems',
                           'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously',
                           'seven', 'several', 'shall', 'shant', 'she', 'shed', 'shell', 'shes',
                           'should', 'shouldnt', 'since', 'six', 'so', 'some', 'somebody', 'someday',
                           'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat',
                           'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying',
                           'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'taking',
                           'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that',
                           'thatll', 'thats', 'thats', 'thatve', 'the', 'their', 'theirs', 'them',
                           'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby',
                           'thered', 'therefore', 'therein', 'therell', 'therere', 'theres',
                           'theres', 'thereupon', 'thereve', 'these', 'they', 'theyd', 'theyll',
                           'theyre', 'theyve', 'thing', 'things', 'think', 'third', 'thirty',
                           'this', 'thorough', 'thoroughly', 'those', 'though', 'three',
                           'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together',
                           'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try',
                           'trying', 'ts', 'twice', 'two', 'un', 'under', 'underneath', 'undoing',
                           'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up',
                           'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using',
                           'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz',
                           'vs', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome',
                           'well', 'well', 'went', 'were', 'were', 'werent', 'weve', 'what',
                           'whatever', 'whatll', 'whats', 'whatve', 'when', 'whence', 'whenever',
                           'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres',
                           'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while',
                           'whilst', 'whither', 'who', 'whod', 'whoever', 'whole', 'wholl',
                           'whom', 'whomever', 'whos', 'whose', 'why', 'will', 'willing', 'wish',
                           'with', 'within', 'without', 'wonder', 'wont', 'would', 'wouldnt',
                           'yes', 'yet', 'you', 'youd', 'youll', 'your', 'youre', 'yours',
                           'yourself', 'yourselves', 'youve', 'zero', 'a', 'hows', 'i', 'whens',
                           'whys', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o',
                           'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'i', 'www',
                           'amount', 'bill', 'bottom', 'call', 'computer', 'con', 'couldnt',
                           'cry', 'de', 'describe', 'detail', 'due', 'eleven', 'empty', 'fifteen',
                           'fifty', 'fill', 'find', 'fire', 'forty', 'front', 'full', 'give',
                           'hasnt', 'herse', 'himse', 'interest', 'itse', 'mill', 'move', 'myse',
                           'part', 'put', 'show', 'side', 'sincere', 'sixty', 'system', 'ten',
                           'thick', 'thin', 'top', 'twelve', 'twenty', 'abst', 'accordance',
                           'act', 'added', 'adopted', 'affected', 'affecting', 'affects', 'ah',
                           'announce', 'anymore', 'apparently', 'approximately', 'aren', 'arent',
                           'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol',
                           'briefly', 'ca', 'date', 'ed', 'effect', 'etal', 'ff', 'fix', 'gave',
                           'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im', 'immediately',
                           'importance', 'important', 'index', 'information', 'invention', 'itd',
                           'keys', 'kg', 'km', 'largely', 'lets', 'line', 'll', 'means', 'mg',
                           'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted',
                           'obtain', 'obtained', 'omitted', 'ord', 'owing', 'page', 'pages',
                           'poorly', 'possibly', 'potentially', 'pp', 'predominantly', 'present',
                           'previously', 'primarily', 'promptly', 'proud', 'quickly', 'ran',
                           'readily', 'ref', 'refs', 'related', 'research', 'resulted',
                           'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes',
                           'showed', 'shown', 'showns', 'shows', 'significant', 'significantly',
                           'similar', 'similarly', 'slightly', 'somethan', 'specifically',
                           'state', 'states', 'stop', 'strongly', 'substantially', 'successfully',
                           'sufficiently', 'suggest', 'thered', 'thereof', 'therere', 'thereto',
                           'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til',
                           'tip', 'ts', 'ups', 'usefully', 'usefulness', 've', 'vol', 'vols',
                           'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words',
                           'world', 'youd', 'youre']
       
           
            words1 = word1.split(' ')   #split words
           
            keys_list2=[]
            punc = '''!()-'"[]0123—4”567889{};:"\,’<“>""./?@#$%^&*_~'''  #punctuations

            for i in words1:
                i = i.lower()
                i=i.replace("\n"," ")
                for ele in i:
                    if ele in punc:                 #removing punctuation
                        i = i.replace(ele, "")
                if i not in stop_words:  # removing stop words
                     keys_list2.append(i)
                
            
            
            
            dictionary_word = {}
            
            new=""
            for x in range(len(keys_list2)-2):              
                new=keys_list2[x]+" "+keys_list2[x+1]
                if new not in dictionary_word:           
                    dictionary_word[new]=1          ##otherwise just add it in
                else:
                    dictionary_word[new]+=1         #  #If it's in it, the key is incremented by one.
                new=""
            sorted_words = dict(sorted(dictionary_word.items(), key=operator.itemgetter(1), reverse=True))  # sorting words
            
            file_for_write = open(File_Output, "w")                     #writing output to txt file
            file_for_write.write("| WORD         |    WORD     |\n"
                  "| ORDER        |    ORDER    |\n"
                  "| FREQUENCY    |    SEQUENCE |\n\n")
            counter=0
            file_for_write.close()
            file_append=open(File_Output, "a")
            for i in sorted_words:        #writing txt for first 100 word
                file_append.write("{:7}          {:15}\n".format(sorted_words[i],i))
                counter+=1
                if counter==100: 
                    break
        except :#buraya yönlendirir
            print("File not Found!")
            
        file.close()
    
    else:
        print("Invalid word order!!")

def Word_Order_Frequency_Two_Books(Book_1, Book_2, Word_Order, File_Output):
    if Word_Order==1:
        
        try:
            file = open(Book_1, "r", encoding="utf-8-sig")       #reading file operations
            file4 = open(Book_2, "r", encoding="utf-8-sig")
            stop_words = ['able', 'about', 'above', 'abroad', "\n", 'according', "", 'accordingly',
                          'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against',
                          'ago', 'ahead', 'aint', 'all', 'allow', 'allows', 'almost', 'alone',
                          'along', 'alongside', 'already', 'also', 'although', 'always', 'am',
                          'amid', 'amidst', 'among', 'amongst', 'an', 'and', 'another', 'any',
                          'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways',
                          'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are',
                          'arent', 'around', 'as', 'as', 'aside', 'ask', 'asking', 'associated',
                          'at', 'available', 'away', 'awfully', 'back', 'backward', 'backwards',
                          'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been',
                          'before', 'beforehand', 'begin', 'behind', 'being', 'believe', 'below',
                          'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both',
                          'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', 'cant',
                          'caption', 'cause', 'causes', 'certain', 'certainly', 'changes',
                          'clearly', 'cmon', 'co', 'co', 'com', 'come', 'comes', 'concerning',
                          'consequently', 'consider', 'considering', 'contain', 'containing',
                          'contains', 'corresponding', 'could', 'couldnt', 'course', 'cs',
                          'currently', 'dare', 'darent', 'definitely', 'described', 'despite',
                          'did', 'didnt', 'different', 'directly', 'do', 'does', 'doesnt',
                          'doing', 'done', 'dont', 'down', 'downwards', 'during', 'each', 'edu',
                          'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end',
                          'ending', 'enough', 'entirely', 'especially', 'et', 'etc', 'even',
                          'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything',
                          'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far',
                          'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed',
                          'following', 'follows', 'for', 'forever', 'former', 'formerly',
                          'forth', 'forward', 'found', 'four', 'from', 'further', 'furthermore',
                          'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going',
                          'gone', 'got', 'gotten', 'greetings', 'had', 'hadnt', 'half',
                          'happens', 'hardly', 'has', 'hasnt', 'have', 'havent', 'having', 'he',
                          'hed', 'hell', 'hello', 'help', 'hence', 'her', 'here', 'hereafter',
                          'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes',
                          'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit',
                          'however', 'hundred', 'id', 'ie', 'if', 'ignored', 'ill', 'im',
                          'immediate', 'in', 'inasmuch', 'inc', 'inc', 'indeed', 'indicate',
                          'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead',
                          'into', 'inward', 'is', 'isnt', 'it', 'itd', 'itll', 'its', 'its',
                          'itself', 'ive', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'known',
                          'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least',
                          'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'likewise',
                          'little', 'look', 'looking', 'looks', 'low', 'lower', 'ltd', 'made',
                          'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'maynt', 'me',
                          'mean', 'meantime', 'meanwhile', 'merely', 'might', 'mightnt', 'mine',
                          'minus', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs',
                          'much', 'must', 'mustnt', 'my', 'myself', 'name', 'namely', 'nd',
                          'near', 'nearly', 'necessary', 'need', 'neednt', 'needs', 'neither',
                          'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine',
                          'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone',
                          'noone', 'nor', 'normally', 'not', 'nothing', 'notwithstanding',
                          'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh',
                          'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'ones', 'only',
                          'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought',
                          'oughtnt', 'our', 'ours', 'ourselves', 'out', 'outside', 'over',
                          'overall', 'own', 'particular', 'particularly', 'past', 'per',
                          'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably',
                          'probably', 'provided', 'provides', 'que', 'quite', 'qv', 'rather',
                          'rd', 're', 'really', 'reasonably', 'recent', 'recently', 'regarding',
                          'regardless', 'regards', 'relatively', 'respectively', 'right',
                          'round', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second',
                          'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems',
                          'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously',
                          'seven', 'several', 'shall', 'shant', 'she', 'shed', 'shell', 'shes',
                          'should', 'shouldnt', 'since', 'six', 'so', 'some', 'somebody', 'someday',
                          'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat',
                          'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying',
                          'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'taking',
                          'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that',
                          'thatll', 'thats', 'thats', 'thatve', 'the', 'their', 'theirs', 'them',
                          'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby',
                          'thered', 'therefore', 'therein', 'therell', 'therere', 'theres',
                          'theres', 'thereupon', 'thereve', 'these', 'they', 'theyd', 'theyll',
                          'theyre', 'theyve', 'thing', 'things', 'think', 'third', 'thirty',
                          'this', 'thorough', 'thoroughly', 'those', 'though', 'three',
                          'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together',
                          'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try',
                          'trying', 'ts', 'twice', 'two', 'un', 'under', 'underneath', 'undoing',
                          'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up',
                          'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using',
                          'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz',
                          'vs', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome',
                          'well', 'well', 'went', 'were', 'were', 'werent', 'weve', 'what',
                          'whatever', 'whatll', 'whats', 'whatve', 'when', 'whence', 'whenever',
                          'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres',
                          'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while',
                          'whilst', 'whither', 'who', 'whod', 'whoever', 'whole', 'wholl',
                          'whom', 'whomever', 'whos', 'whose', 'why', 'will', 'willing', 'wish',
                          'with', 'within', 'without', 'wonder', 'wont', 'would', 'wouldnt',
                          'yes', 'yet', 'you', 'youd', 'youll', 'your', 'youre', 'yours',
                          'yourself', 'yourselves', 'youve', 'zero', 'a', 'hows', 'i', 'whens',
                          'whys', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o',
                          'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'i', 'www',
                          'amount', 'bill', 'bottom', 'call', 'computer', 'con', 'couldnt',
                          'cry', 'de', 'describe', 'detail', 'due', 'eleven', 'empty', 'fifteen',
                          'fifty', 'fill', 'find', 'fire', 'forty', 'front', 'full', 'give',
                          'hasnt', 'herse', 'himse', 'interest', 'itse', 'mill', 'move', 'myse',
                          'part', 'put', 'show', 'side', 'sincere', 'sixty', 'system', 'ten',
                          'thick', 'thin', 'top', 'twelve', 'twenty', 'abst', 'accordance',
                          'act', 'added', 'adopted', 'affected', 'affecting', 'affects', 'ah',
                          'announce', 'anymore', 'apparently', 'approximately', 'aren', 'arent',
                          'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol',
                          'briefly', 'ca', 'date', 'ed', 'effect', 'etal', 'ff', 'fix', 'gave',
                          'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im', 'immediately',
                          'importance', 'important', 'index', 'information', 'invention', 'itd',
                          'keys', 'kg', 'km', 'largely', 'lets', 'line', 'll', 'means', 'mg',
                          'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted',
                          'obtain', 'obtained', 'omitted', 'ord', 'owing', 'page', 'pages',
                          'poorly', 'possibly', 'potentially', 'pp', 'predominantly', 'present',
                          'previously', 'primarily', 'promptly', 'proud', 'quickly', 'ran',
                          'readily', 'ref', 'refs', 'related', 'research', 'resulted',
                          'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes',
                          'showed', 'shown', 'showns', 'shows', 'significant', 'significantly',
                          'similar', 'similarly', 'slightly', 'somethan', 'specifically',
                          'state', 'states', 'stop', 'strongly', 'substantially', 'successfully',
                          'sufficiently', 'suggest', 'thered', 'thereof', 'therere', 'thereto',
                          'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til',
                          'tip', 'ts', 'ups', 'usefully', 'usefulness', 've', 'vol', 'vols',
                          'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words',
                          'world', 'youd', 'youre']

            word1 = file.read()
            words1 = word1.split(' ')
            dictionary_word1 = {}
            punc = '''!()-'"[]01234567889{};:"\,’<“>""./?@#$%^&*_~'''

            for i in words1:
                i = i.lower()
                i=i.replace("\n","")
                for ele in i:
                    if ele in punc:
                        i = i.replace(ele, "")                   #removing punctuations
                if i in dictionary_word1 and i not in stop_words:  # removing stop words
                    dictionary_word1[i] += 1
                elif i not in stop_words:                     #If it's in it, it increases your key by one.
                    dictionary_word1[i] = 1                   #otherwise add it in
            sorted_words1 = {}
            sorted_words1 = dict(sorted(dictionary_word1.items(), key=operator.itemgetter(1), reverse=True))  # sorting words

            word2 = file4.read()
            words2 = word2.split(' ')
            dictionary_word2 = {}

            for i in words2:
                i = i.lower()
                for ele in i:
                    if ele in punc:
                        i = i.replace(ele, "")                    #removing punctuations
                if i in dictionary_word2 and i not in stop_words:  # removing stop words
                    dictionary_word2[i] += 1
                elif i not in stop_words:
                    dictionary_word2[i] = 1
         
                
            sorted_words2 = {}
            sorted_words2 = dict(sorted(dictionary_word2.items(), key=operator.itemgetter(1), reverse=True))  # sorting words
           
            counter = 0

            all_sorted_words = {}                                           #If there are words in the same order, 
            for word in sorted_words1:                                      #it collects their keys, otherwise 
                all_sorted_words[word] = sorted_words1[word]                #it puts the key as 1 in the dictionary.

            for word in sorted_words2:
                if word in all_sorted_words:
                    all_sorted_words[word] += sorted_words2[word]
                else:
                    all_sorted_words[word] = sorted_words2[word]

            all_sorted_words1 = dict(sorted(all_sorted_words.items(), key=operator.itemgetter(1), reverse=True))
            file_write=open(File_Output,"w")
            file_write.write("| TOTAL     | BOOK 1     | BOOK 2     | WORD     |\n"
                  "| ORDER     | ORDER      | ORDER      | ORDER    |\n"
                  "| FREQUENCY | FREQUENCY  | FREQUENCY  | SEQUENCE |\n"
                  )
            counter = 0
            file_write.close()
            file_append=open(File_Output,"a")               #Writing output to txt file
            for word in all_sorted_words1:
                counter += 1
                if word not in sorted_words1:            #If the other book does not have the same word, it will set the key to 0.
                    sorted_words1[word] = 0
                elif word not in sorted_words2:
                    sorted_words2[word] = 0
                if counter == 100:
                    break
                file_append.write("{:10} {:11} {:11}      {:11}\n".format(all_sorted_words1[word], sorted_words1[word],
                                                           sorted_words2[word],
                                                           word))
            file_append.close()
        except:
            print("File not Found!")
            
       
        
            
    elif Word_Order==2:
        try: 
           file = open(Book_1, "r", encoding="utf-8-sig")          #file operations
           file2 = open(Book_2, "r", encoding="utf-8-sig")
           stop_words = ['able', 'about', 'above', 'abroad', "\n", 'according', "", 'accordingly',
                         'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against',
                         'ago', 'ahead', 'aint', 'all', 'allow', 'allows', 'almost', 'alone',
                         'along', 'alongside', 'already', 'also', 'although', 'always', 'am',
                         'amid', 'amidst', 'among', 'amongst', 'an', 'and', 'another', 'any',
                         'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways',
                         'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are',
                         'arent', 'around', 'as', 'as', 'aside', 'ask', 'asking', 'associated',
                         'at', 'available', 'away', 'awfully', 'back', 'backward', 'backwards',
                         'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been',
                         'before', 'beforehand', 'begin', 'behind', 'being', 'believe', 'below',
                         'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both',
                         'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', 'cant',
                         'caption', 'cause', 'causes', 'certain', 'certainly', 'changes',
                         'clearly', 'cmon', 'co', 'co', 'com', 'come', 'comes', 'concerning',
                         'consequently', 'consider', 'considering', 'contain', 'containing',
                         'contains', 'corresponding', 'could', 'couldnt', 'course', 'cs',
                         'currently', 'dare', 'darent', 'definitely', 'described', 'despite',
                         'did', 'didnt', 'different', 'directly', 'do', 'does', 'doesnt',
                         'doing', 'done', 'dont', 'down', 'downwards', 'during', 'each', 'edu',
                         'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end',
                         'ending', 'enough', 'entirely', 'especially', 'et', 'etc', 'even',
                         'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything',
                         'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far',
                         'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed',
                         'following', 'follows', 'for', 'forever', 'former', 'formerly',
                         'forth', 'forward', 'found', 'four', 'from', 'further', 'furthermore',
                         'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going',
                         'gone', 'got', 'gotten', 'greetings', 'had', 'hadnt', 'half',
                         'happens', 'hardly', 'has', 'hasnt', 'have', 'havent', 'having', 'he',
                         'hed', 'hell', 'hello', 'help', 'hence', 'her', 'here', 'hereafter',
                         'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes',
                         'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit',
                         'however', 'hundred', 'id', 'ie', 'if', 'ignored', 'ill', 'im',
                         'immediate', 'in', 'inasmuch', 'inc', 'inc', 'indeed', 'indicate',
                         'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead',
                         'into', 'inward', 'is', 'isnt', 'it', 'itd', 'itll', 'its', 'its',
                         'itself', 'ive', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'known',
                         'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least',
                         'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'likewise',
                         'little', 'look', 'looking', 'looks', 'low', 'lower', 'ltd', 'made',
                         'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'maynt', 'me',
                         'mean', 'meantime', 'meanwhile', 'merely', 'might', 'mightnt', 'mine',
                         'minus', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs',
                         'much', 'must', 'mustnt', 'my', 'myself', 'name', 'namely', 'nd',
                         'near', 'nearly', 'necessary', 'need', 'neednt', 'needs', 'neither',
                         'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine',
                         'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone',
                         'noone', 'nor', 'normally', 'not', 'nothing', 'notwithstanding',
                         'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh',
                         'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'ones', 'only',
                         'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought',
                         'oughtnt', 'our', 'ours', 'ourselves', 'out', 'outside', 'over',
                         'overall', 'own', 'particular', 'particularly', 'past', 'per',
                         'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably',
                         'probably', 'provided', 'provides', 'que', 'quite', 'qv', 'rather',
                         'rd', 're', 'really', 'reasonably', 'recent', 'recently', 'regarding',
                         'regardless', 'regards', 'relatively', 'respectively', 'right',
                         'round', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second',
                         'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems',
                         'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously',
                         'seven', 'several', 'shall', 'shant', 'she', 'shed', 'shell', 'shes',
                         'should', 'shouldnt', 'since', 'six', 'so', 'some', 'somebody', 'someday',
                         'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat',
                         'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying',
                         'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'taking',
                         'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that',
                         'thatll', 'thats', 'thats', 'thatve', 'the', 'their', 'theirs', 'them',
                         'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby',
                         'thered', 'therefore', 'therein', 'therell', 'therere', 'theres',
                         'theres', 'thereupon', 'thereve', 'these', 'they', 'theyd', 'theyll',
                         'theyre', 'theyve', 'thing', 'things', 'think', 'third', 'thirty',
                         'this', 'thorough', 'thoroughly', 'those', 'though', 'three',
                         'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together',
                         'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try',
                         'trying', 'ts', 'twice', 'two', 'un', 'under', 'underneath', 'undoing',
                         'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up',
                         'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using',
                         'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz',
                         'vs', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome',
                         'well', 'well', 'went', 'were', 'were', 'werent', 'weve', 'what',
                         'whatever', 'whatll', 'whats', 'whatve', 'when', 'whence', 'whenever',
                         'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres',
                         'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while',
                         'whilst', 'whither', 'who', 'whod', 'whoever', 'whole', 'wholl',
                         'whom', 'whomever', 'whos', 'whose', 'why', 'will', 'willing', 'wish',
                         'with', 'within', 'without', 'wonder', 'wont', 'would', 'wouldnt',
                         'yes', 'yet', 'you', 'youd', 'youll', 'your', 'youre', 'yours',
                         'yourself', 'yourselves', 'youve', 'zero', 'a', 'hows', 'i', 'whens',
                         'whys', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o',
                         'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'i', 'www',
                         'amount', 'bill', 'bottom', 'call', 'computer', 'con', 'couldnt',
                         'cry', 'de', 'describe', 'detail', 'due', 'eleven', 'empty', 'fifteen',
                         'fifty', 'fill', 'find', 'fire', 'forty', 'front', 'full', 'give',
                         'hasnt', 'herse', 'himse', 'interest', 'itse', 'mill', 'move', 'myse',
                         'part', 'put', 'show', 'side', 'sincere', 'sixty', 'system', 'ten',
                         'thick', 'thin', 'top', 'twelve', 'twenty', 'abst', 'accordance',
                         'act', 'added', 'adopted', 'affected', 'affecting', 'affects', 'ah',
                         'announce', 'anymore', 'apparently', 'approximately', 'aren', 'arent',
                         'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol',
                         'briefly', 'ca', 'date', 'ed', 'effect', 'etal', 'ff', 'fix', 'gave',
                         'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im', 'immediately',
                         'importance', 'important', 'index', 'information', 'invention', 'itd',
                         'keys', 'kg', 'km', 'largely', 'lets', 'line', 'll', 'means', 'mg',
                         'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted',
                         'obtain', 'obtained', 'omitted', 'ord', 'owing', 'page', 'pages',
                         'poorly', 'possibly', 'potentially', 'pp', 'predominantly', 'present',
                         'previously', 'primarily', 'promptly', 'proud', 'quickly', 'ran',
                         'readily', 'ref', 'refs', 'related', 'research', 'resulted',
                         'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes',
                         'showed', 'shown', 'showns', 'shows', 'significant', 'significantly',
                         'similar', 'similarly', 'slightly', 'somethan', 'specifically',
                         'state', 'states', 'stop', 'strongly', 'substantially', 'successfully',
                         'sufficiently', 'suggest', 'thered', 'thereof', 'therere', 'thereto',
                         'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til',
                         'tip', 'ts', 'ups', 'usefully', 'usefulness', 've', 'vol', 'vols',
                         'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words',
                         'world', 'youd', 'youre']

           word1 = file.read()                #reading file
           words1 = word1.split(' ')          #split words
           dictionary_word1 = {}
           keys_list2=[]
           punc = '''!()-'"[]0123—4”567889{};:"\,’<“>""./?@#$%^&*_~'''  #punctuations

           for i in words1:
               i = i.lower()
               i=i.replace("\n"," ")
               for ele in i:
                   if ele in punc:                #removing punctuations
                       i = i.replace(ele, "")
               if i not in stop_words:                 # removing stop words
                    keys_list2.append(i)
               
           
           
           
           dictionary_word4 = {}
           
           new=""
           for x in range(len(keys_list2)-2):           #throwing consecutive words into tupple
               new=keys_list2[x]+" "+keys_list2[x+1] 
               if new not in dictionary_word4:           
                   dictionary_word4[new]=1            #If it's not in it, the key is equals 1 .
               else:
                   dictionary_word4[new]+=1          #If it's in it, the key is incremented by one.
               new=""
           sorted_words4 = dict(sorted(dictionary_word4.items(), key=operator.itemgetter(1), reverse=True))  # sorting words
          
         
         
           word2 = file2.read()             #reading file
           words2 = word2.split(' ')         #split words
           key_list = []

           for i in words2:
               i = i.lower()             #makes all lowercase
               for ele in i:
                   if ele in punc:
                       i = i.replace(ele, "") #removing punctuations
               if i  not in stop_words:  # removing stop words
                   key_list.append(i)
              
           
          
           dictionary_word3 = {}
           
           new=""
           for x in range(len(key_list)-2):            #puts words into the dictionary
               new=key_list[x]+" "+key_list[x+1]
               if new not in dictionary_word3:           
                   dictionary_word3[new]= 1            #otherwise  throw it in dictionary
               else:
                   dictionary_word3[new]+=1            #Increases the key by one if it's in it
               new=""
           sorted_words3 = dict(sorted(dictionary_word3.items(), key=operator.itemgetter(1), reverse=True))  # sorting words
           
               
       
          
           counter = 0

           all_sorted_words = {}                                  #if it contains the same  words it collects their keys
           for word in sorted_words3:
               all_sorted_words[word] = sorted_words3[word]

           for word in sorted_words4:
               if word in all_sorted_words:
                   all_sorted_words[word] += sorted_words4[word]
               else:
                   all_sorted_words[word] = sorted_words4[word]

           all_sorted_words1 = dict(sorted(all_sorted_words.items(), key=operator.itemgetter(1), reverse=True))#sorting words
           file_write=open(File_Output,"w")
           file_write.write("| TOTAL     | BOOK 1     | BOOK 2     | WORD     |\n"
                 "| ORDER     | ORDER      | ORDER      | ORDER    |\n"
                 "| FREQUENCY | FREQUENCY  | FREQUENCY  | SEQUENCE |\n"
                 )
           counter = 0
           file_write.close()
           file_append=open(File_Output,"a")
           for word in all_sorted_words1:       #Writes the first 100 elements of the txt file
               counter += 1
               if word not in sorted_words3:
                   sorted_words3[word] = 0
               elif word not in sorted_words4:
                   sorted_words4[word] = 0
               if counter == 100:
                   break
               file_append.write("{:10} {:11} {:11}      {:11}\n".format(all_sorted_words1[word], sorted_words4[word],
                                                          sorted_words3[word],
                                                          word))
           file_append.close()
        except:
           print("File not Found!")#sends an error message
        
           
    else:
        print("İnvalid word order !")



