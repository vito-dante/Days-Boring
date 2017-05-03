package Calculate

import "testing"

func TestMyadd(test *testing.T) {
	value := myadd(15, 12)
	if value != 27 {
		test.Error("it expect 30 it did receive", value)
	}
}
