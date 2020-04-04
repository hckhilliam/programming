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

  public static void solve(int test) {
    var parts = Console.ReadLine().Split(' ');
    int n = Convert.ToInt32(parts[0]);
    int k = Convert.ToInt32(parts[1]);
    int p = Convert.ToInt32(parts[2]);
    var allBeauties = new int[n,k];
    for (int i = 0; i < n; ++i) {
      var beauties = Console.ReadLine().Split(' ');
      for (int j = 0; j < beauties.Length; ++j) {
        allBeauties[i,j] = Convert.ToInt32(beauties[j]);
      }
    }

    // dp[p][n] is max beauty using p plates on n stacks
    var dp = new int[p+1,n];
    int sum = 0;
    for (int i = 1; i <= p; ++i) {
      if (i <= k) sum += allBeauties[0,i-1];
      dp[i,0] = sum;
    }

    for (int i = 1; i <= p; ++i) {
      for (int j = 1; j < n; ++j) {
        // Max of allBeauties[j][k] + dp[i-k][j-1] for all k = 0..i
        sum = 0;
        for (int l = 0; l < i; ++l) {
          if (l < k) sum += allBeauties[j,l];
          dp[i,j] = Math.Max(sum + dp[i-l-1,j-1], Math.Max(dp[i,j-1], dp[i,j]));
        }
      }
    }

    Console.WriteLine($"Case #{test+1}: {dp[p,n-1]}");
  }
}

Program.Main(null);