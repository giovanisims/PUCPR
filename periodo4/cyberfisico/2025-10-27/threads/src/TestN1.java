

public class TestN1 {

    public static void simulateN1Model(int threadCount) {
        System.out.println("--- Simulating " + threadCount + " tasks ---");

        long startTime = System.currentTimeMillis();

        // Using run() directly will make all threads run sequentially.
        for (int i = 0; i < threadCount; i++) {
            Task task = new Task();
            task.run();
        }

        long endTime = System.currentTimeMillis();
        System.out.println("Total Time: " + (endTime - startTime) + " ms");
    }

}
