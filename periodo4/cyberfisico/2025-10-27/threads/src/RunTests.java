

public class RunTests {
    public static void main(String[] args) {
        // since each thread is doing the exact same task giving it more tasks is like giving it more threads
        int[] numThreadsCount = {10, 100, 500, 1000};

        System.out.println("Starting N:M Test");
        for (int threadCount : numThreadsCount) {
            TestNM.simulateNModel(threadCount, Runtime.getRuntime().availableProcessors());
        }
        System.out.println("Finished N:M Test");
        System.out.println("--------------------");
        System.out.println("Starting 1:1 Test");
        for  (int threadCount : numThreadsCount) {
            Test11.simulate11Model(threadCount);
        }
        System.out.println("Finished 1:1 Test");
    }
}
