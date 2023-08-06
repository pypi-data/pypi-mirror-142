# MySecrets v1.0.4

## 1. Introduction

    This package includes three parts: hash, symmetrical encryption and jtc64
    (jtc64 is similar to base64, convert every 3 hex digits to 2 64-bit characters to reduce the length)
    
    The algorithm of hash and symmetrical encryption is very secure.
    
    Hash: If the original text changes slightly, the hash will be completely different.
          Known some part of the original text, you cannot get the other part reversely.

    Symmetrical encryption: Given ciphertext and some part of plaintext, you cannot get the key or other part of plaintext.
                            Given several ciphertext and corresponding plaintext, you cannot get the key.
    
## 2. Usage
    
### (1) Hash

    getHash(text:str)
    
    The return value format is a str with 64 hex digits.
    
### (2) Jtc64

    strToJtc64(text:str), jtc64ToStr(text:str)
    hexToJtc64(text:str), jtc64ToHex(text:str)
    
    The jtc64 output is a str containing 0~9, a~z, A~Z, @, # or $,%,&,= in the last.
    
    If the input/output is hex, note that it should be 0~9 and a~f in str, a~f should be in lower case, no "0x" at first.
    
### (3) Symmetrical encryption

    encrypt(text:str,key:str)
    decrypt(text:str,key:str)
    
    text: the str you want to encrypt (in encrypt) or the encrypted data (in decrypt) (the length must be larger than 0)
    key: any password you like
    
    The encrypted data is in jtc64 format.

## 3. Algorithms

### (1) Hash

    Step 1: Convert original text to hex
    Step 2: Add the length of hex data (in decimalism) to the last of hex data
    Step 2: Supple the length of hex data to the multiple of 128 by adding '0' at first
    Step 3: Convert every 128 digits to 64 digits by adding a 128-digit hex number, then multipling with a 192-digit hex number
            and then taking the mid 64 digits, until it becomes 64 digits.
            If the length is not the multiple of 128, add 64 '0' at first.
            In the adding process, just add digit by digit, no carry.
            The 128-digit and 192-digit hex number is randomly generated when I write the program, it is a fixed number.
    Step 4: We finally get a 64-digit hex in step 3. Then create 20 groups, each group deal with this 64-digit hex in following process:
            ① add a 64-digit hex digit by digit
            ② disorder the digits of the hex text according to the pre-generated rule
            ③ multiple it with a 128-digit hex number, then take the mid 64 digits
            ④ disorder the digits of the hex text according to the rule in ②
            (Note: the 64-digit hex in ①, the 128-digit hex number in ③ and the rule in ② are randomly generated when I write the program, they are fixed)
    Step 5: Add the 20 64-digit hex numbers digit by digit, the result is the final hash.
    
    (You can see the pre-generated things in hash.py or others/standard.txt)
    
### (2) Jtc64

    Jtc64 is mainly composed of these characters: '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#'
    Each character stands for the number of its location. e.g. 0 stands for 0, b stands for 11, Z stands for 61
    Step 1: Convert original text to hex
    Step 2: Each time take 3 digits, calculate num, num = first digit * 256 + second digit * 16 + third digit
            num1 = num // 64; num2 = num % 64, convert num1 and num2 to corresponding jtc64 characters and put them together
            All 3 hex digits convert to 2 jtc64 characters, then combine the jtc64 characters in the original order
    Step 3: If there is no remaining hex digits, the convertion ends.
            If 1 hex digit remains, add it to the last of jtc64 str directly.
            If 2 hex digits remain, calculate num, num = first digit * 166 + second digit, num1 = num // 4; num2 = num % 4
            Add the jtc64 character corresponding to num1 to the last of jtc64 str, $ % & = each stands for 0,1,2,3 in num2, add it to the last of jtc64 str

### (3) Symmetrical encryption

    Step 1: Get the hash of the key, let it be the key in later program
    Step 2: Generate a random 32-digit hex value
            (You can also generate it with other methods or even give a specific value, but it cannot be same in two encryptions)
    Step 3: Get the hash of the text, take first 16 digits, add it to the last of the text
    Step 4: Generate the secret with the same length to text by using key and the random 32-digit hex value in following process:
            ① divide into n parts (n=length//64 or length//64+1) (depend on whether it is multiple of 64)
            ② for each part, get the hash of partNumber+ran+key (ran is the random 32-digit hex value) (partNumber starts from 0)
            ③ combine the hash of all parts, and then remove the last several digits to make the length same to text
    Step 5: Add the text and the secret digit by digit
    Step 6: Add the random 32-digit hex to the first of the result in step 5
    Step 7: Get the hash of the result in step 6, add the hash to the first of it
    Step 8: Add '0' in the last (to represent mode or version, because the program may update or add other mode later)
    Step 9: Convert it to jtc64

## 4. Why it is secuse

### (1) Hash
    
① 128-digit times with 192-digit or 64-digit times with 128-digit, even only change one digit in the original text, the middle 64 digits will be completely different, so this ensures the randomtivity of the hash.

② Divide the last 64-digit hex into 20 groups, deal with them, then add together. Since we add 20 numbers together, we cannot get what each of them is. And we also need to add a 64-digit hex first, disorder them and times with another 128-digit hex, then disorder them. Then in each group, the result doesn't have any regularity to the original data. Then add them together, you cannot get the original text reversely.

### (2) Symmetrical encryption

① Is my key safe?

Known plaintext and ciphertext, we can only get the secret. But the secret is composed of a lot of hashes, as proved above, we cannot get the original text from hash.

② Known ciphertext and some part of plaintext, can I get other part of plaintext?

The secret is composed of a lot of hashes. If we know some part of plaintext, we can get these parts of hashes. But the original text of each hash is all different (need to add the partNumber), and we cannot get the original text from hash, so we cannot know other part of hashes.

③ Known several ciphertext and corresponding plaintext, then can I get the plaintext from another ciphertext that I want to decipher?

When encrypting each time, we need to generate a different random number, we need to include it when calculating the hash. So the secret of each ciphertext is diffferent, there is no definite relationship between plaintext and ciphertext.

## 5. LICENSE

    Source code part follows GPL v2.
    
    The algorithm of hash, symmetrical encryption and jtc64 follows the following rule:
        (The algorithm here means the pattern of encrypting and encoding, not the specific process of encrypting or encoding)
        
        Any part of the algorithm cannot be modified. (Including but not limited to: basic way, 
            the usage of characters, the information of digit operation and digit exchange, multiplier,
            the original string of hash, the location of each content, version information and checking method)
        That is, you must obey the following rules:
            ① Calculating the hash of same str with your program and with my program, the result is same.
            ② The data encrypted by your program, can be decrypted normally by my program and get the correct data.
            ③ The data encrypted by my program, can be decrypted normally by your program and get the correct data.
            ④ Encoding the same str of hex data to jtc64, with your program and with my program, the result is same.
            ⑤ Decoding the same jtc64 data with your program and with my program, the result is same.
            ⑥ If the input ciphertext or jtc64 data is invalid, your program must be able to report errors or not work normally.
        (Note: about the random 32-digit hex number generated when encrypting, you can use different ways to generate it,
            but it must be in the same length and format and randomized enough)
            
        If only using the algorithm, it can be casually used for commercial or sold, no attribution is required for any use.

    源代码部分使用 GPL v2 开源协议
    
    Hash、对称加密、jtc64算法部分需遵循以下协议：
        （这里的算法指的是加密方式或编码方式，而不是实现加密或编码的过程）
        
        算法不得进行任何修改（包括但不限于：基本方式、字符的使用、位运算信息、位交换信息、乘数、哈希原始字符串、各部分内容位置、版本信息、校验方式）
        即必须保证如下事项：
            ① 相同的字符串，使用您的软件和使用我的软件计算，得到的哈希值是相同的
            ② 经过您的软件加密的内容，使用我的软件可以正常解密并获得正确的内容
            ③ 经过我的软件加密的内容，使用您的软件可以正常解密并获得正确的内容
            ④ 相同的字符串或16进制数据，使用您的软件和使用我的软件进行 jtc64 编码，得到的结果是相同的
            ⑤ 相同的 jtc64 编码数据，使用您的软件和使用我的软件进行解码，得到的结果是相同的
            ⑥ 如果输入的密文或 jtc64 编码数据是非法的，您的软件必须能够报错或不能正常运行
        （注：在加密过程中随机生成的32位16进制数，您可以使用不同的生成方式，但必须保证位数和格式相同且足够随机）
        
        如果只使用算法，可以随意进行商业使用或进行出售，任何使用均无需注明出处。

## 6. Others

    Emial: jtc1246@outlook.com
    Requirement: Python 3
    Installation: pip3 install mySecrets
