using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

public class Program
{
  public static void Main(string[] args)
  {
    UndergroundSystem undergroundSystem = new UndergroundSystem();
    undergroundSystem.CheckIn(45, "Leyton", 3);
    undergroundSystem.CheckIn(32, "Paradise", 8);
    undergroundSystem.CheckIn(27, "Leyton", 10);
    undergroundSystem.CheckOut(45, "Waterloo", 15);
    undergroundSystem.CheckOut(27, "Waterloo", 20);
    undergroundSystem.CheckOut(32, "Cambridge", 22);
    Console.WriteLine(undergroundSystem.GetAverageTime("Paradise", "Cambridge"));       // return 14.0. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
    Console.WriteLine(undergroundSystem.GetAverageTime("Leyton", "Waterloo"));          // return 11.0. There were two travels from "Leyton" to "Waterloo", a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.0
    undergroundSystem.CheckIn(10, "Leyton", 24);
    Console.WriteLine(undergroundSystem.GetAverageTime("Leyton", "Waterloo"));          // return 11.0
    undergroundSystem.CheckOut(10, "Waterloo", 38);
    Console.WriteLine(undergroundSystem.GetAverageTime("Leyton", "Waterloo"));          // return 12.0
  }

  public class UndergroundSystem {
    private Dictionary<string, int> trackerSum;
    private Dictionary<string, int> trackerCount;
    private Dictionary<int, Tuple<string, int>> checkIns;

    public UndergroundSystem() {
        this.trackerSum = new Dictionary<string, int>();
        this.trackerCount = new Dictionary<string, int>();
        this.checkIns = new Dictionary<int, Tuple<string, int>>();
    }

    public void CheckIn(int id, string stationName, int t) {
      if (this.checkIns.ContainsKey(id)) return;
      this.checkIns[id] = new Tuple<string, int>(stationName, t);
    }

    public void CheckOut(int id, string stationName, int t) {
      if (!this.checkIns.ContainsKey(id)) return;
      var checkIn = this.checkIns[id];
      string pair = $"{checkIn.Item1}-{stationName}";
      if (this.trackerSum.ContainsKey(pair)) {
        this.trackerSum[pair] += t - checkIn.Item2;
        ++this.trackerCount[pair];
      } else {
        this.trackerSum[pair] = t - checkIn.Item2;
        this.trackerCount[pair] = 1;
      }
      this.checkIns.Remove(id);
    }

    public double GetAverageTime(string startStation, string endStation) {
      string pair = $"{startStation}-{endStation}";
      if (!this.trackerSum.ContainsKey(pair)) return 0;
      return this.trackerSum[pair] * 1.0/this.trackerCount[pair];
    }
  }
}

Program.Main(null);
