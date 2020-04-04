using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

public class Program
{
  public static void Main(string[] args)
  {
    int t = Convert.ToInt32(Console.ReadLine());
    for (int i = 0; i < t; ++i) {
      solve(i);
    }
  }

  public static void solve(int test)
  {
    var parts = Console.ReadLine().Split(' ');
    int b = Convert.ToInt32(parts[1]);
    var a = Console.ReadLine().Split(' ')
      .Select(x => Convert.ToInt32(x)).ToList()
      .OrderBy(x => x);
    int ans = 0;
    foreach (int p in a) {
      b -= p;
      if (b < 0) break;
      ++ans;
    }

    Console.WriteLine($"Case #{test + 1}: {ans}");
  }
}

Program.Main(null);
