using System;
using System.Text;

namespace CTFChallenge
{
    class Program
    {
        static void Main(string[] args)
        {
            // Encoded string
            string encodedString = "VlhDT1hJW2tdI2FhIE9SIGdheU8iICIkbQ==";
            Console.WriteLine($"Encoded String: {encodedString}");
            Console.WriteLine($"There seems to somthing wrong in the code check the code");

            // Call the Decode function to decode the string step by step
            string decodedString = Decode(encodedString);

            Console.WriteLine($"Decoded String: {decodedString}");
            Console.WriteLine($"Hint: Check the code");
        }

        static string Decode(string String_res)
        {
	    // Step 3: Caesar Cipher Decrypt with a shift of -5
            String_res = CaesarCipher(String_res, -5);
            Console.WriteLine($"Decrypted: {String_res}");
            
            // Step 1: Base64 Decode
            String_res = Base64Decode(String_res);
            Console.WriteLine($"Decoded: {String_res}");

            // Step 2: XOR Decrypt with Hex key 0x10
            String_res = XORDecrypt(String_res, 0x10);
            Console.WriteLine($"Decrypted: {String_res}");

            return String_res;
        }

        static string Base64Decode(string encodedText)
        {
            byte[] base64EncodedBytes = Convert.FromBase64String(encodedText);
            return Encoding.UTF8.GetString(base64EncodedBytes);
        }

        static string XORDecrypt(string input, int key)
        {
            StringBuilder decoded = new StringBuilder();
            foreach (char c in input)
            {
                decoded.Append((char)(c ^ key));
            }
            return decoded.ToString();
        }

        static string CaesarCipher(string input, int shift)
        {
            StringBuilder result = new StringBuilder();
            foreach (char c in input)
            {
                if (char.IsLetter(c))
                {
                    char offset = char.IsUpper(c) ? 'A' : 'a';
                    char decryptedChar = (char)(((c - offset + shift + 26) % 26) + offset);
                    result.Append(decryptedChar);
                }
                else
                {
                    result.Append(c); // Non-alphabet characters remain the same
                }
            }
            return result.ToString();
        }
    }
}


