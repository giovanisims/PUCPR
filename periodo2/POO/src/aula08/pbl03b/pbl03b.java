package aula08.pbl03b;

public class pbl03b {
    public static void main(String[] args){
        Employee empregado1 = new Employee("João","Masculino", 39, "Logistica");
        Employee empregado2 = new Employee("Maria","Feminino", 29, "Desenvolvimento");
        Employee empregado3 = new Employee("Cris","Feminino", 69, "Gerenciamento");

        System.out.print(empregado1.getEmployee());
        System.out.print(empregado2.getEmployee());
        System.out.print(empregado3.getEmployee());
    }
}

class Employee {
    String name;
    String sex;
    int age;
    String department;
    double salary;

    Employee(String name, String sex, int age, String department){
        this.name = name;
        this.sex = sex;
        this.age = age;
        this.department = department;
        switch (department) {
            case "Logistica":
                this.salary = 1000;
                break;
            case "Desenvolvimento":
                this.salary = 5000;
                break;
            case "Gerenciamento":
                this.salary = 10000;
                break;
        }

    }

    String getEmployee() {
        return String.format("Nome: %s | Sexo: %s | Idade: %s | Departamento: %s | Salario: %s \n",
                name, sex, age, department, salary);
    }
}