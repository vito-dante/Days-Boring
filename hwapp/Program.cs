using System;

namespace ConsoleApplication
{
    public class Program : Father
    {
        public static void Main(string[] args)
        {
            Program some = new Program();
            some.Something2();
        }
    }
}
