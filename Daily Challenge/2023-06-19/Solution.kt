class Solution {
    fun largestAltitude(gain: IntArray): Int {
        var largest: Int = 0;
        var currAlt: Int = 0;
        for (g in gain) {
            currAlt += g;
            if(currAlt > largest) largest = currAlt;
        }
        return largest;
    }
}