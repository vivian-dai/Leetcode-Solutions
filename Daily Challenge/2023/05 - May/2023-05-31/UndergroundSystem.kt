class UndergroundSystem() {
    val times = hashMapOf<String, MutableList<Int>>();
    val checkedIn = hashMapOf<Int, List<Any>>();

    fun checkIn(id: Int, stationName: String, t: Int) {
        checkedIn.put(id, listOf(stationName, t));
    }

    fun checkOut(id: Int, stationName: String, t: Int) {
        val time = checkedIn.get(id)?.get(1) as Int;
        val station = checkedIn.get(id)?.get(0);
        if(!times.containsKey("${station} ${stationName}")) {
            times.put("${station} ${stationName}", mutableListOf<Int>())
        }
        if (time != null && station != null) {
            times["${station} ${stationName}"]?.add(t - time)
        }
    }

    fun getAverageTime(startStation: String, endStation: String): Double {
        var total: Double = 0.0;
        val key = "${startStation} ${endStation}";
        if (times!!.get(key) != null && times!!.get(key)!!.isNotEmpty()) {
            var total = 0.0
            for (num in times!!.get(key)!!) {
                total += num;
            }
            return total / times!!.get(key)!!.size;
        }
        return total;
    }

}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * var obj = UndergroundSystem()
 * obj.checkIn(id,stationName,t)
 * obj.checkOut(id,stationName,t)
 * var param_3 = obj.getAverageTime(startStation,endStation)
 */
 