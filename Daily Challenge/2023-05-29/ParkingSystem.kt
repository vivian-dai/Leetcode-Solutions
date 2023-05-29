class ParkingSystem(big: Int, medium: Int, small: Int) {
    var big = big;
    var medium = medium;
    var small = small;

    fun addCar(carType: Int): Boolean {
        return when (carType) {
            1 -> big-- > 0
            2 -> medium-- > 0
            else -> small-- > 0
        }
    }

}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * var obj = ParkingSystem(big, medium, small)
 * var param_1 = obj.addCar(carType)
 */
 