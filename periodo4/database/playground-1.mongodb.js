
// --- Conectar ao banco de dados 'ecommerce' --- //
use('ecommerce');

print('Iniciando a criação das coleções com validação de schema...');

print('Removendo coleções existentes...');
db.users.drop();
db.categories.drop();
db.products.drop();
db.orders.drop();

// --- 1. Coleção: users --- //
print('Criando coleção "users"...');
db.createCollection("users", {
    validator: {
        $jsonSchema: {
            bsonType: "object", // Isso é redundante já que o BSON de nível superior é sempre "object"
            title: "User Object Validation",
            required: ["name", "email", "password", "address"],
            properties: { // Define cada atributo na tabela
                name: {
                    bsonType: "string",
                    minLength: 2, // "minLength" para texto e "minimum" para números
                    description: "'name' deve ser uma string e é obrigatório"
                },
                email: {
                    bsonType: "string",
                    description: "'email' deve ser uma string e é obrigatório",
                    // Você pode definir regex para validação customizada
                    pattern: '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$',
                },
                password: {
                    bsonType: "string",
                    description: "'password' deve ser uma string e é obrigatório",
                    minLength: 6
                },
                address: {
                    bsonType: "object",
                    description: "'address' deve ser um objeto",
                    required: ["CEP", "State", "City", "Street", "Number"],
                    properties: {
                        CEP: { bsonType: "string" },
                        State: { bsonType: "string" },
                        City: { bsonType: "string" },
                        Street: { bsonType: "string" },
                        Number: { bsonType: "string" }
                    }
                },
                geolocation: {
                    bsonType: "object",
                    description: "'geolocation' deve ser um objeto GeoJSON",
                    required: ["type", "coordinates"],
                    properties: {
                        type: {
                            enum: ["Point"],
                            description: "Deve ser do tipo 'Point'"
                        },
                        coordinates: {
                            bsonType: "array",
                            description: "Deve ser um array de [longitude, latitude]",
                            minItems: 2,
                            maxItems: 2,
                            items: { bsonType: "double" }
                        }
                    }
                },
                fidelityPoints: {
                    bsonType: "number",
                    description: "'fidelityPoints' deve ser um número"
                }
            }
        }
    },
    validationLevel: "strict",  // ou "moderate" (valida apenas em atualizações)
    validationAction: "error"   // ou "warn" (registra aviso mas permite inserção)
});

// --- 2. Coleção: categories --- //
print('Criando coleção "categories"...');
db.createCollection("categories", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            title: "Category Object Validation",
            required: ["name"],
            properties: {
                name: {
                    bsonType: "string",
                    description: "'name' deve ser uma string e é obrigatório"
                },
                subcategories: {
                    bsonType: "array",
                    description: "'subcategories' deve ser um array de objetos",
                    items: {
                        bsonType: "object",
                        required: ["name"],
                        properties: {
                            name: { bsonType: "string" }
                        }
                    }
                }
            }
        }
    },
    validationAction: "error",
    validationLevel: "strict"
});

// --- 3. Coleção: products --- //
print('Criando coleção "products"...');
db.createCollection("products", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            title: "Product Object Validation",
            required: ["name", "price", "quantity", "categoryId", "userId"],
            properties: {
                name: {
                    bsonType: "string",
                    description: "'name' deve ser uma string e é obrigatório"
                },
                description: {
                    bsonType: "string",
                    description: "'description' deve ser uma string"
                },
                price: {
                    bsonType: "double",
                    description: "'price' deve ser um double e é obrigatório"
                },
                quantity: {
                    bsonType: "int",
                    description: "'quantity' deve ser um inteiro e é obrigatório"
                },
                Location: {
                    bsonType: "string",
                    description: "'Location' deve ser uma string"
                },
                categoryId: {
                    bsonType: "objectId",
                    description: "'categoryId' é uma referência e é obrigatório"
                },
                userId: {
                    bsonType: "objectId",
                    description: "'userId' (vendedor) é uma referência e é obrigatório"
                },
                ratings: {
                    bsonType: "array",
                    description: "'ratings' deve ser um array de objetos de avaliação",
                    items: {
                        bsonType: "object",
                        required: ["userId", "rating", "date"],
                        properties: {
                            userId: { bsonType: "objectId" },
                            rating: {
                                bsonType: "number",
                                minimum: 1,
                                maximum: 5
                            },
                            review: { bsonType: "string" },
                            vendorReply: { bsonType: "string" },
                            reply: { bsonType: "string" },
                            date: { bsonType: "date" }
                        }
                    }
                }
            }
        }
    },
    validationAction: "error",
    validationLevel: "strict"
});

// --- 4. Coleção: orders --- //
print('Criando coleção "orders"...');
db.createCollection("orders", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            title: "Order Object Validation",
            required: ["userId", "products", "status", "date"],
            properties: {
                userId: {
                    bsonType: "objectId",
                    description: "'userId' (comprador) é uma referência e é obrigatório"
                },
                products: {
                    bsonType: "array",
                    description: "Um pedido deve ter pelo menos um produto",
                    minItems: 1,
                    items: {
                        bsonType: "object",
                        required: ["productId", "quantity", "price"],
                        properties: {
                            productId: { bsonType: "objectId" },
                            quantity: {
                                bsonType: "int",
                                minimum: 1
                            },
                            price: { bsonType: "double" } // Preço "snapshot" no momento da compra
                        }
                    }
                },
                status: {
                    enum: ["Pending", "Processing", "Shipped", "Delivered", "Cancelled"],
                    description: "Status deve ser um dos valores permitidos"
                },
                date: {
                    bsonType: "date",
                    description: "'date' é obrigatório"
                },
                generatedPoints: {
                    bsonType: "number",
                    description: "'generatedPoints' deve ser um número"
                }
            }
        }
    },
    validationAction: "error",
    validationLevel: "strict"
});

print('--- Criação de coleções concluída com sucesso! ---');


// --- Inserção de dados --- //

print('Iniciando inserção de dados de exemplo...');

// --- Inserindo Usuários --- //
print('Inserindo usuários...');
const usersResult = db.users.insertMany([
    {
        name: "João Silva",
        email: "joao.silva@email.com",
        password: "Senha@123",
        address: {
            CEP: "80010-000",
            State: "PR",
            City: "Curitiba",
            Street: "Rua XV de Novembro",
            Number: "100"
        },
        geolocation: {
            type: "Point",
            coordinates: [-49.2732, -25.4195]
        },
        fidelityPoints: 150
    },
    {
        name: "Maria Santos",
        email: "maria.santos@email.com",
        password: "Senha@456",
        address: {
            CEP: "01310-100",
            State: "SP",
            City: "São Paulo",
            Street: "Avenida Paulista",
            Number: "1000"
        },
        geolocation: {
            type: "Point",
            coordinates: [-46.6577, -23.5613]
        },
        fidelityPoints: 320
    },
    {
        name: "Pedro Oliveira",
        email: "pedro.oliveira@email.com",
        password: "Senha@789",
        address: {
            CEP: "30130-010",
            State: "MG",
            City: "Belo Horizonte",
            Street: "Avenida Afonso Pena",
            Number: "500"
        },
        geolocation: {
            type: "Point",
            coordinates: [-43.9378, -19.9167]
        },
        fidelityPoints: 75
    },
    {
        name: "Ana Costa",
        email: "ana.costa@email.com",
        password: "Senha@012",
        address: {
            CEP: "40020-000",
            State: "BA",
            City: "Salvador",
            Street: "Rua Chile",
            Number: "200"
        },
        geolocation: {
            type: "Point",
            coordinates: [-38.5108, -12.9714]
        },
        fidelityPoints: 250
    },
    {
        name: "Carlos Mendes",
        email: "carlos.mendes@email.com",
        password: "Senha@345",
        address: {
            CEP: "20040-020",
            State: "RJ",
            City: "Rio de Janeiro",
            Street: "Avenida Rio Branco",
            Number: "156"
        },
        geolocation: {
            type: "Point",
            coordinates: [-43.1729, -22.9068]
        },
        fidelityPoints: 420
    }
]);

const userIds = Object.values(usersResult.insertedIds);
print(`${userIds.length} usuários inseridos com sucesso!`);

// --- Inserindo Categorias --- //
print('Inserindo categorias...');
const categoriesResult = db.categories.insertMany([
    {
        name: "Electronics",
        subcategories: [
            { name: "Laptops" },
            { name: "Smartphones" },
            { name: "Tablets" }
        ]
    },
    {
        name: "Books",
        subcategories: [
            { name: "Fiction" },
            { name: "Non-Fiction" },
            { name: "Academic" }
        ]
    },
    {
        name: "Clothing",
        subcategories: [
            { name: "Men" },
            { name: "Women" },
            { name: "Kids" }
        ]
    },
    {
        name: "Home & Garden",
        subcategories: [
            { name: "Furniture" },
            { name: "Decor" },
            { name: "Garden Tools" }
        ]
    },
    {
        name: "Sports",
        subcategories: [
            { name: "Fitness" },
            { name: "Outdoor" },
            { name: "Team Sports" }
        ]
    }
]);

const categoryIds = Object.values(categoriesResult.insertedIds);
print(`${categoryIds.length} categorias inseridas com sucesso!`);

// --- Inserindo Produtos --- //
print('Inserindo produtos...');
const productsResult = db.products.insertMany([
    {
        name: "Premium Laptop",
        description: "High-performance laptop with 16GB RAM and 512GB SSD",
        price: 3500.00,
        quantity: 15,
        Location: "Curitiba - PR",
        categoryId: categoryIds[0], // Electronics
        userId: userIds[0], // João Silva (vendedor)
        ratings: [
            {
                userId: userIds[1],
                rating: 5,
                review: "Excelente produto, superou minhas expectativas!",
                vendorReply: "Obrigado pelo feedback!",
                date: new Date("2024-10-15")
            },
            {
                userId: userIds[2],
                rating: 4,
                review: "Muito bom, apenas a entrega demorou um pouco.",
                date: new Date("2024-11-01")
            }
        ]
    },
    {
        name: "Classic Fiction Novel",
        description: "Bestselling fiction book of the year",
        price: 45.90,
        quantity: 50,
        Location: "São Paulo - SP",
        categoryId: categoryIds[1], // Books
        userId: userIds[1], // Maria Santos (vendedor)
        ratings: [
            {
                userId: userIds[3],
                rating: 5,
                review: "História incrível, não consegui parar de ler!",
                date: new Date("2024-10-20")
            }
        ]
    },
    {
        name: "Sports Running Shoes",
        description: "Comfortable running shoes for all terrains",
        price: 299.90,
        quantity: 30,
        Location: "Belo Horizonte - MG",
        categoryId: categoryIds[4], // Sports
        userId: userIds[2], // Pedro Oliveira (vendedor)
        ratings: [
            {
                userId: userIds[0],
                rating: 4,
                review: "Confortável, mas poderia ter mais opções de cores.",
                vendorReply: "Obrigado! Em breve teremos novas cores disponíveis.",
                date: new Date("2024-10-25")
            },
            {
                userId: userIds[4],
                rating: 5,
                review: "Perfeito para corridas longas!",
                date: new Date("2024-11-05")
            }
        ]
    },
    {
        name: "Wooden Coffee Table",
        description: "Elegant wooden coffee table with modern design",
        price: 850.00,
        quantity: 8,
        Location: "Salvador - BA",
        categoryId: categoryIds[3], // Home & Garden
        userId: userIds[3], // Ana Costa (vendedor)
        ratings: [
            {
                userId: userIds[1],
                rating: 5,
                review: "Qualidade excepcional, ficou perfeita na sala!",
                date: new Date("2024-10-30")
            }
        ]
    },
    {
        name: "Cotton T-Shirt",
        description: "100% cotton comfortable t-shirt",
        price: 59.90,
        quantity: 100,
        Location: "Rio de Janeiro - RJ",
        categoryId: categoryIds[2], // Clothing
        userId: userIds[4], // Carlos Mendes (vendedor)
        ratings: [
            {
                userId: userIds[2],
                rating: 4,
                review: "Tecido de boa qualidade, o tamanho é fiel.",
                date: new Date("2024-11-02")
            },
            {
                userId: userIds[3],
                rating: 5,
                review: "Muito confortável e o preço é justo.",
                date: new Date("2024-11-08")
            }
        ]
    },
    {
        name: "Smartphone Pro Max",
        description: "Latest smartphone with advanced camera system",
        price: 4500.00,
        quantity: 20,
        Location: "Curitiba - PR",
        categoryId: categoryIds[0], // Electronics
        userId: userIds[0], // João Silva (vendedor)
        ratings: []
    },
    {
        name: "Academic Physics Book",
        description: "Comprehensive physics textbook for university students",
        price: 180.00,
        quantity: 25,
        Location: "São Paulo - SP",
        categoryId: categoryIds[1], // Books
        userId: userIds[1], // Maria Santos (vendedor)
        ratings: [
            {
                userId: userIds[4],
                rating: 5,
                review: "Excelente material didático!",
                date: new Date("2024-10-18")
            }
        ]
    }
]);

const productIds = Object.values(productsResult.insertedIds);
print(`${productIds.length} produtos inseridos com sucesso!`);

// --- Inserindo Pedidos --- //
print('Inserindo pedidos...');
const ordersResult = db.orders.insertMany([
    {
        userId: userIds[1], // Maria Santos (comprador)
        products: [
            {
                productId: productIds[0], // Premium Laptop
                quantity: 1,
                price: 3500.00
            }
        ],
        status: "Delivered",
        date: new Date("2024-10-10"),
        generatedPoints: 350
    },
    {
        userId: userIds[2], // Pedro Oliveira (comprador)
        products: [
            {
                productId: productIds[1], // Classic Fiction Novel
                quantity: 2,
                price: 45.90
            },
            {
                productId: productIds[4], // Cotton T-Shirt
                quantity: 3,
                price: 59.90
            }
        ],
        status: "Shipped",
        date: new Date("2024-10-28"),
        generatedPoints: 27
    },
    {
        userId: userIds[0], // João Silva (comprador)
        products: [
            {
                productId: productIds[2], // Sports Running Shoes
                quantity: 1,
                price: 299.90
            }
        ],
        status: "Processing",
        date: new Date("2024-11-03"),
        generatedPoints: 30
    },
    {
        userId: userIds[4], // Carlos Mendes (comprador)
        products: [
            {
                productId: productIds[0], // Premium Laptop
                quantity: 1,
                price: 3500.00
            },
            {
                productId: productIds[5], // Smartphone Pro Max
                quantity: 1,
                price: 4500.00
            }
        ],
        status: "Pending",
        date: new Date("2024-11-09"),
        generatedPoints: 800
    },
    {
        userId: userIds[3], // Ana Costa (comprador)
        products: [
            {
                productId: productIds[3], // Wooden Coffee Table
                quantity: 1,
                price: 850.00
            }
        ],
        status: "Delivered",
        date: new Date("2024-10-22"),
        generatedPoints: 85
    },
    {
        userId: userIds[1], // Maria Santos (comprador)
        products: [
            {
                productId: productIds[6], // Academic Physics Book
                quantity: 1,
                price: 180.00
            },
            {
                productId: productIds[1], // Classic Fiction Novel
                quantity: 1,
                price: 45.90
            }
        ],
        status: "Cancelled",
        date: new Date("2024-11-01"),
        generatedPoints: 0
    }
]);

const orderIds = Object.values(ordersResult.insertedIds);
print(`${orderIds.length} pedidos inseridos com sucesso!`);

print('--- Inserção de dados concluída com sucesso! ---');
print(`Total inserido: ${userIds.length} usuários, ${categoryIds.length} categorias, ${productIds.length} produtos, ${orderIds.length} pedidos`);


// --- Consultas Sprint 1 --- //

// --- 1. Encontrar todos os produtos de uma categoria específica --- //

// Primeiro, encontramos o ID da categoria que queremos
const category = db.categories.findOne({ name: "Electronics" });

if (category) {
  const categoryId = category._id;
  
  print(`Buscando produtos para a Categoria ID: ${categoryId}`);
  
  // Agora, usamos esse ID para encontrar todos os produtos correspondentes
  const products = db.products.find({ categoryId: categoryId });
  
  // Imprime os resultados
  products.forEach(product => {
    printjson(product);
  });
  
} else {
  print("Categoria 'Electronics' não encontrada.");
}

// --- 2. Buscar todas as avaliações de um produto --- //

// Busca o primeiro produto que tenha avaliações
const productWithRatings = db.products.findOne({ "ratings.0": { $exists: true } });

if (productWithRatings) {
  const productIdToFind = productWithRatings._id;
  
  print(`Buscando avaliações para o Produto: ${productWithRatings.name} (ID: ${productIdToFind})`);
  
  // Usamos findOne para o produto e projeção { ratings: 1 } para retornar APENAS o array de ratings
  // _id: 0 remove o campo _id do resultado para um output mais limpo
  const result = db.products.findOne(
    { _id: productIdToFind },
    { projection: { _id: 0, name: 1, ratings: 1 } }
  );
  
  if (result && result.ratings) {
    print("Avaliações encontradas:");
    printjson(result.ratings);
  } else {
    print("Produto não possui avaliações.");
  }
} else {
  print("Nenhum produto com avaliações foi encontrado.");
}

// --- 3. Criar uma nova transação (compra) --- //

// Obtém IDs reais do banco de dados
const customer = db.users.findOne({}, { _id: 1 });
const products = db.products.find({}).limit(2).toArray();

if (customer && products.length >= 2) {
  const customerId = customer._id;
  const product1Id = products[0]._id;
  const product2Id = products[1]._id;
  
  // Montamos o documento do pedido
  const newOrder = {
    userId: customerId,
    products: [
      {
        productId: product1Id,
        quantity: 1,
        price: products[0].price // "Snapshot" do preço no momento da compra
      },
      {
        productId: product2Id,
        quantity: 2,
        price: products[1].price 
      }
    ],
    status: "Pending", // Status inicial, conforme nosso schema enum
    date: new Date(),
    generatedPoints: Math.floor((products[0].price + (products[1].price * 2)) / 10)
  };
  
  try {
    const insertResult = db.orders.insertOne(newOrder);
    print("Pedido criado com sucesso!");
    print(`Novo Order ID: ${insertResult.insertedId}`);
    printjson(newOrder);
    
  } catch (e) {
    print("ERRO ao criar pedido:");
    printjson(e); // Isso mostrará erros de validação se houver
  }
} else {
  print("Não foi possível obter dados para criar o pedido.");
}

// --- 4. Atualizar quantidade de produto após uma compra --- //

// Obtém os primeiros 2 produtos do banco para simular uma compra
const productsForUpdate = db.products.find({}).limit(2).toArray();

if (productsForUpdate.length >= 2) {
  const itemsPurchased = [
    {
      productId: productsForUpdate[0]._id,
      quantity: 1
    },
    {
      productId: productsForUpdate[1]._id,
      quantity: 2
    }
  ];
  
  print("Preparando para atualizar estoque...");
  print(`Produto 1: ${productsForUpdate[0].name} - Quantidade atual: ${productsForUpdate[0].quantity}`);
  print(`Produto 2: ${productsForUpdate[1].name} - Quantidade atual: ${productsForUpdate[1].quantity}`);
  
  // Criamos um array de operações de atualização
  const operations = itemsPurchased.map(item => {
    return {
      updateOne: {
        filter: { _id: item.productId }, // Encontra o produto pelo ID
        update: {
          $inc: { quantity: -item.quantity } // Decrementa a quantidade em estoque
        }
      }
    };
  });
  
  // Executamos todas as operações em lote
  try {
    const bulkResult = db.products.bulkWrite(operations);
    
    print("Estoque atualizado com sucesso!");
    print(`Documentos modificados: ${bulkResult.modifiedCount}`);
    
    // Mostra as quantidades atualizadas
    const updatedProducts = db.products.find({ 
      _id: { $in: itemsPurchased.map(item => item.productId) } 
    }).toArray();
    
    print("\nQuantidades após atualização:");
    updatedProducts.forEach(p => {
      print(`${p.name}: ${p.quantity} unidades`);
    });
    
  } catch (e) {
    print("ERRO ao atualizar estoque:");
    printjson(e);
  }
} else {
  print("Não há produtos suficientes no banco para realizar a atualização.");
}