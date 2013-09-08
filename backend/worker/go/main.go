package main

/* import "scenario" */
import "time"
import "fmt"
import "net/http"
import "io/ioutil"

const Concurrency = 100
const Requests = 10
var Total int = 0


func Run() string{
    url := "https://beta.smplmchn.com/users/18/"
    resp, _ := http.Get(url)
    body, _ := ioutil.ReadAll(resp.Body)
    return string(body)
}

func RunTest(num int) {
    for i := 0; i < num; i++ {
        Run()
    }
    Total++;
}


func main() {
    fmt.Println("Started")
    startTime := time.Now()
    for i := 0; i < Concurrency; i++ {
        go RunTest(Requests)
    }
    for {
        if Total == Concurrency {
            break
        }
        time.Sleep(100*time.Millisecond)
    }

    endTime := time.Now()

    fmt.Println(startTime)
    fmt.Println(endTime)
    fmt.Println("Done")
}
