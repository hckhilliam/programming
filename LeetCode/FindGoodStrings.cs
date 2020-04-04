using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

public class Program
{
  public static void Main(string[] args)
  {
    Console.WriteLine(FindGoodStrings(2, "aa", "da", "b"));
    Console.WriteLine(FindGoodStrings(8, "leetcode", "leetgoes", "leet"));
    Console.WriteLine(FindGoodStrings(2, "gx", "gz", "x"));
    Console.WriteLine(FindGoodStrings(3, "aaa", "ada", "b"));
  }

    public static int FindGoodStrings(int n, string s1, string s2, string evil) {
      long goodStrings = 0;
      long modulo = 1000000007;
      int index = 0;
      for (; index < n; ++index) if (s2[index] != s1[index]) break;

      if (n - index == 1) {
        goodStrings += s2[index] - s1[index] + 1;
      } else {
        int diff = s2[index] - s1[index] - 1; // -1 if len=1
        long intermediateCount = 0;
        if (diff > 0) {
          intermediateCount = 1;
          for (int i = index; i < n - 1; ++i) {
              intermediateCount = (intermediateCount * 26) % modulo; // 25 if len=1
          }
          intermediateCount = (intermediateCount * diff) % modulo;
        }
        goodStrings = (goodStrings + intermediateCount) % modulo;
        Console.WriteLine($"1: {goodStrings}");

        for (int i = index + 1; i < n; ++i) {
          diff = s2[i] - 'a' + 1;
          intermediateCount = 1;
          for (int j = i; j < n - 1; ++j) {
            intermediateCount = (intermediateCount * 26) % modulo;
          }
          intermediateCount = (intermediateCount * diff) % modulo;
          goodStrings = (goodStrings + intermediateCount) % modulo;
        }
        Console.WriteLine($"2: {goodStrings}");

        for (int i = index + 1; i < n; ++i) {
          diff = 'z' - s1[i] + 1;
          intermediateCount = 1;
          for (int j = i; j < n - 1; ++j) {
            intermediateCount = (intermediateCount * 26) % modulo;
          }
          intermediateCount = (intermediateCount * diff) % modulo;
          goodStrings = (goodStrings + intermediateCount) % modulo;
        }
        Console.WriteLine($"3: {goodStrings}");
      }
      return (int) goodStrings;
    }
}

Program.Main(null);
