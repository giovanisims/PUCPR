// Nome dos integrantes:
// Giovani Nota Simões
// Livia Oliveira Rosembach
// Lucas Brisch

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
            bsonType: "object",
            title: "User Object Validation",
            required: ["name", "email", "password", "address"],
            additionalProperties: true,
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
                            maxItems: 2
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
                    bsonType: ["double", "int"],
                    description: "'price' deve ser um número e é obrigatório"
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
                            price: { bsonType: ["double", "int"] } // Preço "snapshot" no momento da compra
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
        quantity: NumberInt(15),
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
        quantity: NumberInt(50),
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
        quantity: NumberInt(30),
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
        quantity: NumberInt(8),
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
        quantity: NumberInt(100),
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
        quantity: NumberInt(20),
        Location: "Curitiba - PR",
        categoryId: categoryIds[0], // Electronics
        userId: userIds[0], // João Silva (vendedor)
        ratings: []
    },
    {
        name: "Academic Physics Book",
        description: "Comprehensive physics textbook for university students",
        price: 180.00,
        quantity: NumberInt(25),
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
                quantity: NumberInt(1),
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
                quantity: NumberInt(2),
                price: 45.90
            },
            {
                productId: productIds[4], // Cotton T-Shirt
                quantity: NumberInt(3),
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
                quantity: NumberInt(1),
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
                quantity: NumberInt(1),
                price: 3500.00
            },
            {
                productId: productIds[5], // Smartphone Pro Max
                quantity: NumberInt(1),
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
                quantity: NumberInt(1),
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
                quantity: NumberInt(1),
                price: 180.00
            },
            {
                productId: productIds[1], // Classic Fiction Novel
                quantity: NumberInt(1),
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


// --- Criação de Índices para Otimização --- //

print('\n--- Criando índices para otimização de consultas ---');

// Índice em products.categoryId
// Justificativa: Consultas frequentes de produtos por categoria (ex: buscar todos os eletrônicos)
// Cardinalidade média (5 categorias) e alta frequência de uso nas queries
db.products.createIndex({ categoryId: 1 });
print('✓ Índice criado em products.categoryId');

// Índice em products.userId (vendedor)
// Justificativa: Necessário para listar todos os produtos de um vendedor específico
// Cardinalidade média (5 usuários vendedores) e importante para o painel do vendedor
db.products.createIndex({ userId: 1 });
print('✓ Índice criado em products.userId');

// Índice em orders.userId (comprador)
// Justificativa: Consulta de histórico de pedidos do usuário é operação comum
// Alta seletividade e essencial para a experiência do usuário
db.orders.createIndex({ userId: 1 });
print('✓ Índice criado em orders.userId');

// Índice em orders.status
// Justificativa: Filtros por status (Pending, Shipped, etc) são usados em dashboards
// Baixa cardinalidade (5 valores) mas alta frequência de consulta para gestão de pedidos
db.orders.createIndex({ status: 1 });
print('✓ Índice criado em orders.status');

// Índice em orders.date (descendente)
// Justificativa: Consultas por período e ordenação temporal são comuns em relatórios
// Alta seletividade em queries com range e necessário para analytics
db.orders.createIndex({ date: -1 });
print('✓ Índice criado em orders.date (ordem descendente)');

// Índice único em users.email
// Justificativa: Login por email é operação crítica e emails devem ser únicos
// Previne duplicatas e otimiza autenticação (operação de alta frequência)
db.users.createIndex({ email: 1 }, { unique: true });
print('✓ Índice único criado em users.email');

// Índice geoespacial em users.geolocation
// Justificativa: Permite queries de proximidade (ex: usuários ou produtos próximos)
// Essencial para funcionalidades baseadas em localização
db.users.createIndex({ geolocation: "2dsphere" });
print('✓ Índice geoespacial (2dsphere) criado em users.geolocation');

// Índice em categories.name
// Justificativa: Busca de categoria por nome é operação frequente nas consultas
// Alta seletividade (nomes únicos) e melhora performance de lookups
db.categories.createIndex({ name: 1 });
print('✓ Índice criado em categories.name');

print('--- Criação de índices concluída! ---\n');


// --- Consultas Sprint 1 --- //

print('\n==============================================');
print('===    INICIANDO CONSULTAS - SPRINT 1     ===');
print('==============================================\n');

// --- 1. Encontrar todos os produtos de uma categoria específica --- //

print('\n--- CONSULTA 1: Produtos por Categoria ---');
// Primeiro, encontramos o ID da categoria que queremos
const category = db.categories.findOne({ name: "Electronics" });

if (category) {
  const categoryId = category._id;
  
  print(`Buscando produtos para a Categoria: ${category.name} (ID: ${categoryId})`);
  
  // Agora, usamos esse ID para encontrar todos os produtos correspondentes
  const productsQuery1 = db.products.find({ categoryId: categoryId }).toArray();
  
  print(`Total de produtos encontrados: ${productsQuery1.length}`);
  // Imprime os resultados
  productsQuery1.forEach(product => {
    print(`  - ${product.name} (R$ ${product.price}) - Estoque: ${product.quantity}`);
  });
  
} else {
  print("Categoria 'Electronics' não encontrada.");
}

// --- 2. Buscar todas as avaliações de um produto --- //

print('\n--- CONSULTA 2: Avaliações de Produto ---');
// Busca o primeiro produto que tenha avaliações
const productWithRatings = db.products.findOne({ "ratings.0": { $exists: true } });

if (productWithRatings) {
  const productIdToFind = productWithRatings._id;
  
  print(`Buscando avaliações para o Produto: ${productWithRatings.name} (ID: ${productIdToFind})`);
  
  // Usamos findOne para o produto e projeção { ratings: 1 } para retornar APENAS o array de ratings
  const resultQuery2 = db.products.findOne(
    { _id: productIdToFind },
    { projection: { name: 1, ratings: 1 } }
  );
  
  if (resultQuery2 && resultQuery2.ratings) {
    print(`Total de avaliações: ${resultQuery2.ratings.length}`);
    resultQuery2.ratings.forEach((rating, index) => {
      print(`  Avaliação ${index + 1}: ${rating.rating} estrelas - "${rating.review}"`);
      if (rating.vendorReply) {
        print(`    Resposta do vendedor: "${rating.vendorReply}"`);
      }
    });
  } else {
    print("Produto não possui avaliações.");
  }
} else {
  print("Nenhum produto com avaliações foi encontrado.");
}

// --- 3. Criar uma nova transação (compra) --- //

print('\n--- CONSULTA 3: Criar Nova Transação ---');
// Obtém IDs reais do banco de dados
const customer = db.users.findOne({}, { _id: 1, name: 1 });
const productsQuery3 = db.products.find({}).limit(2).toArray();

if (customer && productsQuery3.length >= 2) {
  const customerId = customer._id;
  const product1Id = productsQuery3[0]._id;
  const product2Id = productsQuery3[1]._id;
  
  print(`Cliente: ${customer.name}`);
  print(`Produto 1: ${productsQuery3[0].name} - R$ ${productsQuery3[0].price}`);
  print(`Produto 2: ${productsQuery3[1].name} - R$ ${productsQuery3[1].price} (x2)`);
  
  // Montamos o documento do pedido
  const newOrder = {
    userId: customerId,
    products: [
      {
        productId: product1Id,
        quantity: NumberInt(1),
        price: productsQuery3[0].price // "Snapshot" do preço no momento da compra
      },
      {
        productId: product2Id,
        quantity: NumberInt(2),
        price: productsQuery3[1].price 
      }
    ],
    status: "Pending", // Status inicial, conforme nosso schema enum
    date: new Date(),
    generatedPoints: Math.floor((productsQuery3[0].price + (productsQuery3[1].price * 2)) / 10)
  };
  
  try {
    const insertResult = db.orders.insertOne(newOrder);
    print("✓ Pedido criado com sucesso!");
    print(`  Order ID: ${insertResult.insertedId}`);
    print(`  Pontos gerados: ${newOrder.generatedPoints}`);
    
  } catch (e) {
    print("✗ ERRO ao criar pedido:");
    printjson(e); // Isso mostrará erros de validação se houver
  }
} else {
  print("Não foi possível obter dados para criar o pedido.");
}

// --- 4. Atualizar quantidade de produto após uma compra --- //

print('\n--- CONSULTA 4: Atualizar Estoque ---');
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
  
  print(`Produto 1: ${productsForUpdate[0].name}`);
  print(`  Quantidade ANTES: ${productsForUpdate[0].quantity} unidades`);
  print(`Produto 2: ${productsForUpdate[1].name}`);
  print(`  Quantidade ANTES: ${productsForUpdate[1].quantity} unidades`);
  
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
    
    print("\n✓ Estoque atualizado com sucesso!");
    print(`  Documentos modificados: ${bulkResult.modifiedCount}`);
    
    // Mostra as quantidades atualizadas
    const updatedProducts = db.products.find({ 
      _id: { $in: itemsPurchased.map(item => item.productId) } 
    }).toArray();
    
    print("\nQuantidades DEPOIS da atualização:");
    updatedProducts.forEach(p => {
      print(`  ${p.name}: ${p.quantity} unidades`);
    });
    
  } catch (e) {
    print("✗ ERRO ao atualizar estoque:");
    printjson(e);
  }
} else {
  print("Não há produtos suficientes no banco para realizar a atualização.");
}

// --- 5. Calcular a média de avaliação por produto --- //

print('\n--- CONSULTA 5: Média de Avaliação por Produto ---');
// Usa $unwind para "desnormalizar" o array de ratings e calcular a média por produto
const avgRatingsResult = db.products.aggregate([
  {
    // Desconstrói o array de ratings para processar cada avaliação individualmente
    $unwind: "$ratings"
  },
  {
    // Agrupa por produto e calcula a média das avaliações
    $group: {
      _id: "$_id",
      productName: { $first: "$name" },
      averageRating: { $avg: "$ratings.rating" },
      totalRatings: { $sum: 1 }
    }
  },
  {
    // Ordena por média de avaliação (maior primeiro)
    $sort: { averageRating: -1 }
  }
]).toArray();

print(`Total de produtos com avaliações: ${avgRatingsResult.length}`);
avgRatingsResult.forEach(product => {
  print(`  ${product.productName}: ${product.averageRating.toFixed(2)} estrelas (${product.totalRatings} avaliações)`);
});

// --- 6. Calcular o total de vendas por categoria --- //

print('\n--- CONSULTA 6: Total de Vendas por Categoria ---');
// Junta orders com products e depois agrupa por categoria
const salesByCategoryResult = db.orders.aggregate([
  {
    // Desconstrói o array de produtos do pedido
    $unwind: "$products"
  },
  {
    // Lookup para obter informações do produto (incluindo categoryId)
    $lookup: {
      from: "products",
      localField: "products.productId",
      foreignField: "_id",
      as: "productInfo"
    }
  },
  {
    // Desconstrói o resultado do lookup
    $unwind: "$productInfo"
  },
  {
    // Lookup para obter o nome da categoria
    $lookup: {
      from: "categories",
      localField: "productInfo.categoryId",
      foreignField: "_id",
      as: "categoryInfo"
    }
  },
  {
    // Desconstrói o resultado do lookup de categoria
    $unwind: "$categoryInfo"
  },
  {
    // Agrupa por categoria e calcula o total de vendas
    $group: {
      _id: "$categoryInfo._id",
      categoryName: { $first: "$categoryInfo.name" },
      totalSales: { 
        $sum: { 
          $multiply: ["$products.quantity", "$products.price"] 
        } 
      },
      totalOrders: { $sum: 1 },
      totalItemsSold: { $sum: "$products.quantity" }
    }
  },
  {
    // Ordena por total de vendas (maior primeiro)
    $sort: { totalSales: -1 }
  }
]).toArray();

print(`Total de categorias com vendas: ${salesByCategoryResult.length}`);
salesByCategoryResult.forEach(category => {
  print(`  ${category.categoryName}:`);
  print(`    Receita Total: R$ ${category.totalSales.toFixed(2)}`);
  print(`    Pedidos: ${category.totalOrders}`);
  print(`    Itens Vendidos: ${category.totalItemsSold}`);
});

// --- 7. Relatórios de vendas por vendedor --- //

print('\n--- CONSULTA 7: Relatório de Vendas por Vendedor ---');
// Agrupa vendas por vendedor (userId no product)
const salesByVendorResult = db.orders.aggregate([
  {
    // Desconstrói o array de produtos do pedido
    $unwind: "$products"
  },
  {
    // Lookup para obter informações do produto (incluindo vendedor)
    $lookup: {
      from: "products",
      localField: "products.productId",
      foreignField: "_id",
      as: "productInfo"
    }
  },
  {
    // Desconstrói o resultado do lookup
    $unwind: "$productInfo"
  },
  {
    // Lookup para obter informações do vendedor
    $lookup: {
      from: "users",
      localField: "productInfo.userId",
      foreignField: "_id",
      as: "vendorInfo"
    }
  },
  {
    // Desconstrói o resultado do lookup de vendedor
    $unwind: "$vendorInfo"
  },
  {
    // Agrupa por vendedor e calcula métricas de vendas
    $group: {
      _id: "$vendorInfo._id",
      vendorName: { $first: "$vendorInfo.name" },
      totalRevenue: { 
        $sum: { 
          $multiply: ["$products.quantity", "$products.price"] 
        } 
      },
      totalQuantitySold: { $sum: "$products.quantity" },
      totalOrders: { $sum: 1 },
      productsSold: { 
        $addToSet: "$productInfo.name" 
      }
    }
  },
  {
    // Adiciona campo com contagem de produtos únicos vendidos
    $addFields: {
      uniqueProductsSold: { $size: "$productsSold" }
    }
  },
  {
    // Ordena por receita total (maior primeiro)
    $sort: { totalRevenue: -1 }
  },
  {
    // Remove o array de produtos para limpeza do output
    $project: {
      vendorName: 1,
      totalRevenue: 1,
      totalQuantitySold: 1,
      totalOrders: 1,
      uniqueProductsSold: 1
    }
  }
]).toArray();

print(`Total de vendedores com vendas: ${salesByVendorResult.length}`);
salesByVendorResult.forEach(vendor => {
  print(`  ${vendor.vendorName}:`);
  print(`    Receita Total: R$ ${vendor.totalRevenue.toFixed(2)}`);
  print(`    Quantidade Vendida: ${vendor.totalQuantitySold} unidades`);
  print(`    Pedidos Atendidos: ${vendor.totalOrders}`);
  print(`    Produtos Únicos Vendidos: ${vendor.uniqueProductsSold}`);
});

// --- 8. Adicionar promoção temporária a um produto --- //

print('\n--- CONSULTA 8: Adicionar Promoção Temporária ---');
// Seleciona um produto para aplicar desconto
const productForPromo = db.products.findOne({ name: "Premium Laptop" });

if (productForPromo) {
  // Adiciona campo de promoção com desconto de 15% válido por 30 dias
  const promoResult = db.products.updateOne(
    { _id: productForPromo._id },
    {
      $set: {
        promotion: {
          discountPercent: 15,
          startDate: new Date(),
          endDate: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000), // 30 dias a partir de hoje
          active: true
        }
      }
    }
  );
  
  const priceWithDiscount = productForPromo.price * (1 - 15/100);
  print(`✓ Promoção adicionada ao produto: ${productForPromo.name}`);
  print(`  Preço Original: R$ ${productForPromo.price.toFixed(2)}`);
  print(`  Preço com Desconto: R$ ${priceWithDiscount.toFixed(2)}`);
  print(`  Válida até: ${new Date(Date.now() + 30 * 24 * 60 * 60 * 1000).toISOString().split('T')[0]}`);
}

// --- 10. Atualizar pontos de fidelidade após compra --- //

print('\n--- CONSULTA 10: Atualizar Pontos de Fidelidade ---');
// Busca um pedido recente e adiciona pontos ao usuário
const recentOrder = db.orders.findOne({ status: "Delivered" });

if (recentOrder) {
  const userBefore = db.users.findOne({ _id: recentOrder.userId });
  
  // Adiciona os pontos gerados pela compra ao saldo do usuário
  db.users.updateOne(
    { _id: recentOrder.userId },
    { $inc: { fidelityPoints: recentOrder.generatedPoints } }
  );
  
  const userAfter = db.users.findOne({ _id: recentOrder.userId });
  
  print(`✓ Pontos atualizados para usuário: ${userAfter.name}`);
  print(`  Pontos Antes: ${userBefore.fidelityPoints}`);
  print(`  Pontos Ganhos: ${recentOrder.generatedPoints}`);
  print(`  Pontos Depois: ${userAfter.fidelityPoints}`);
}

// --- 11. Aplicar desconto usando pontos de fidelidade --- //

print('\n--- CONSULTA 11: Usar Pontos como Desconto ---');
// Simula uso de pontos (1 ponto = R$ 0.10 de desconto)
const userWithPoints = db.users.findOne({ fidelityPoints: { $gte: 100 } });

if (userWithPoints) {
  const pointsToUse = 100;
  const discountValue = pointsToUse * 0.10; // 1 ponto = R$ 0.10
  
  print(`Cliente: ${userWithPoints.name}`);
  print(`  Pontos Disponíveis: ${userWithPoints.fidelityPoints}`);
  print(`  Pontos a Usar: ${pointsToUse}`);
  print(`  Desconto Gerado: R$ ${discountValue.toFixed(2)}`);
  print(`  Pontos Restantes: ${userWithPoints.fidelityPoints - pointsToUse}`);
  
  // Deduz os pontos utilizados
  db.users.updateOne(
    { _id: userWithPoints._id },
    { $inc: { fidelityPoints: -pointsToUse } }
  );
  print(`✓ Pontos deduzidos com sucesso!`);
}

// --- 12. Vendedor responde a uma avaliação --- //

print('\n--- CONSULTA 12: Responder Avaliação ---');
// Encontra um produto com avaliação sem resposta do vendedor
const productWithUnrepliedRating = db.products.findOne({
  "ratings": {
    $elemMatch: {
      review: { $exists: true },
      vendorReply: { $exists: false }
    }
  }
});

if (productWithUnrepliedRating) {
  // Adiciona resposta do vendedor à primeira avaliação sem resposta
  const ratingIndex = productWithUnrepliedRating.ratings.findIndex(
    r => r.review && !r.vendorReply
  );
  
  if (ratingIndex !== -1) {
    const vendorReply = "Obrigado pelo seu feedback! Estamos sempre buscando melhorar.";
    
    db.products.updateOne(
      { 
        _id: productWithUnrepliedRating._id,
        "ratings.userId": productWithUnrepliedRating.ratings[ratingIndex].userId
      },
      {
        $set: {
          "ratings.$.vendorReply": vendorReply
        }
      }
    );
    
    print(`✓ Resposta adicionada à avaliação do produto: ${productWithUnrepliedRating.name}`);
    print(`  Avaliação Original: "${productWithUnrepliedRating.ratings[ratingIndex].review}"`);
    print(`  Resposta do Vendedor: "${vendorReply}"`);
  }
}

// --- 13. Buscar produtos por proximidade (geolocalização) --- //

print('\n--- CONSULTA 13: Buscar Produtos por Proximidade ---');
// Busca produtos próximos a um usuário específico (usando localização do vendedor)
const referenceUser = db.users.findOne({ name: "João Silva" });

if (referenceUser && referenceUser.geolocation) {
  const searchRadiusKm = 500; 
  const searchRadiusMeters = searchRadiusKm * 1000;
  
  print(`Buscando produtos em um raio de ${searchRadiusKm} km de ${referenceUser.address.City}, ${referenceUser.address.State}`);
  print(`Coordenadas de referência: [${referenceUser.geolocation.coordinates}]`);
  
  // Busca vendedores próximos usando geolocalização
  const nearbyVendors = db.users.find({
    geolocation: {
      $near: {
        $geometry: referenceUser.geolocation,
        $maxDistance: searchRadiusMeters
      }
    }
  }).toArray();
  
  // Busca produtos desses vendedores
  const vendorIds = nearbyVendors.map(v => v._id);
  const nearbyProducts = db.products.find({
    userId: { $in: vendorIds }
  }).toArray();
  
  print(`✓ Encontrados ${nearbyProducts.length} produtos de ${nearbyVendors.length} vendedores próximos:`);
  
  // Agrupa produtos por vendedor para melhor visualização
  nearbyVendors.forEach(vendor => {
    const vendorProducts = nearbyProducts.filter(p => p.userId.equals(vendor._id));
    if (vendorProducts.length > 0) {
      print(`  ${vendor.name} (${vendor.address.City}, ${vendor.address.State}):`);
      vendorProducts.forEach(product => {
        print(`    - ${product.name} (R$ ${product.price.toFixed(2)})`);
      });
    }
  });
}

// --- 14. Buscar produtos próximos ao usuário dentro de um raio específico --- //

print('\n--- CONSULTA 14: Produtos Próximos ao Usuário (Raio Específico) ---');
// Define o usuário de referência e o raio de busca
const searchUser = db.users.findOne({ name: "Maria Santos" });
const searchRadius = 200; // 200 km

if (searchUser && searchUser.geolocation) {
  print(`Usuário: ${searchUser.name} (${searchUser.address.City}, ${searchUser.address.State})`);
  print(`Raio de busca: ${searchRadius} km`);
  
  // Busca vendedores dentro do raio usando índice geoespacial
  const nearbyVendors = db.users.aggregate([
    {
      $geoNear: {
        near: searchUser.geolocation,
        distanceField: "distance",
        maxDistance: searchRadius * 1000, // Converte km para metros
        spherical: true
      }
    },
    {
      // Lookup para buscar produtos desses vendedores
      $lookup: {
        from: "products",
        localField: "_id",
        foreignField: "userId",
        as: "products"
      }
    },
    {
      // Filtra apenas vendedores que têm produtos
      $match: {
        "products.0": { $exists: true }
      }
    },
    {
      // Desconstrói o array de produtos
      $unwind: "$products"
    },
    {
      // Projeta os campos relevantes
      $project: {
        vendorName: "$name",
        vendorCity: "$address.City",
        vendorState: "$address.State",
        distanceKm: { $divide: ["$distance", 1000] },
        productName: "$products.name",
        productPrice: "$products.price",
        productQuantity: "$products.quantity"
      }
    },
    {
      // Ordena por distância
      $sort: { distanceKm: 1 }
    }
  ]).toArray();
  
  print(`✓ Encontrados ${nearbyVendors.length} produtos disponíveis:`);
  
  // Agrupa por vendedor para melhor visualização
  const vendorMap = {};
  nearbyVendors.forEach(item => {
    if (!vendorMap[item.vendorName]) {
      vendorMap[item.vendorName] = {
        distance: item.distanceKm,
        city: item.vendorCity,
        state: item.vendorState,
        products: []
      };
    }
    vendorMap[item.vendorName].products.push({
      name: item.productName,
      price: item.productPrice
    });
  });
  
  Object.keys(vendorMap).forEach(vendorName => {
    const vendor = vendorMap[vendorName];
    print(`  ${vendorName} - ${vendor.city}, ${vendor.state} (${vendor.distance.toFixed(1)} km)`);
    vendor.products.forEach(product => {
      print(`    - ${product.name}: R$ ${product.price.toFixed(2)}`);
    });
  });
}

// --- 15. Calcular média de distância entre compradores e vendedores --- //

print('\n--- CONSULTA 15: Média de Distância Comprador-Vendedor ---');
// Calcula a distância média entre compradores e vendedores em transações concluídas
const distanceAnalysis = db.orders.aggregate([
  {
    // Filtra apenas pedidos entregues
    $match: { status: "Delivered" }
  },
  {
    // Lookup para obter dados do comprador
    $lookup: {
      from: "users",
      localField: "userId",
      foreignField: "_id",
      as: "buyer"
    }
  },
  {
    $unwind: "$buyer"
  },
  {
    // Desconstrói produtos do pedido
    $unwind: "$products"
  },
  {
    // Lookup para obter dados do produto
    $lookup: {
      from: "products",
      localField: "products.productId",
      foreignField: "_id",
      as: "productInfo"
    }
  },
  {
    $unwind: "$productInfo"
  },
  {
    // Lookup para obter dados do vendedor
    $lookup: {
      from: "users",
      localField: "productInfo.userId",
      foreignField: "_id",
      as: "vendor"
    }
  },
  {
    $unwind: "$vendor"
  },
  {
    // Calcula a distância entre comprador e vendedor usando $geoNear não é possível aqui,
    // então usamos a fórmula de Haversine manualmente (aproximação)
    $project: {
      buyerName: "$buyer.name",
      buyerCity: "$buyer.address.City",
      buyerCoords: "$buyer.geolocation.coordinates",
      vendorName: "$vendor.name",
      vendorCity: "$vendor.address.City",
      vendorCoords: "$vendor.geolocation.coordinates",
      // Cálculo simplificado de distância (não é preciso, mas serve para demonstração)
      // Em produção, use uma função mais precisa ou cálculo no código
      latDiff: {
        $subtract: [
          { $arrayElemAt: ["$buyer.geolocation.coordinates", 1] },
          { $arrayElemAt: ["$vendor.geolocation.coordinates", 1] }
        ]
      },
      lonDiff: {
        $subtract: [
          { $arrayElemAt: ["$buyer.geolocation.coordinates", 0] },
          { $arrayElemAt: ["$vendor.geolocation.coordinates", 0] }
        ]
      }
    }
  },
  {
    // Adiciona estimativa de distância (aproximação simples)
    $addFields: {
      estimatedDistanceKm: {
        $multiply: [
          {
            $sqrt: {
              $add: [
                { $pow: ["$latDiff", 2] },
                { $pow: ["$lonDiff", 2] }
              ]
            }
          },
          111 // Aproximadamente 111 km por grau
        ]
      }
    }
  },
  {
    // Agrupa para calcular a média
    $group: {
      _id: null,
      averageDistance: { $avg: "$estimatedDistanceKm" },
      totalTransactions: { $sum: 1 },
      minDistance: { $min: "$estimatedDistanceKm" },
      maxDistance: { $max: "$estimatedDistanceKm" },
      transactions: {
        $push: {
          buyer: "$buyerName",
          buyerCity: "$buyerCity",
          vendor: "$vendorName",
          vendorCity: "$vendorCity",
          distance: "$estimatedDistanceKm"
        }
      }
    }
  }
]).toArray();

if (distanceAnalysis.length > 0) {
  const stats = distanceAnalysis[0];
  print(`✓ Análise de ${stats.totalTransactions} transações concluídas:`);
  print(`  Distância Média: ${stats.averageDistance.toFixed(2)} km`);
  print(`  Distância Mínima: ${stats.minDistance.toFixed(2)} km`);
  print(`  Distância Máxima: ${stats.maxDistance.toFixed(2)} km`);
  
  print(`\n  Exemplos de transações:`);
  stats.transactions.slice(0, 3).forEach(t => {
    print(`    ${t.buyer} (${t.buyerCity}) ← ${t.vendor} (${t.vendorCity}): ${t.distance.toFixed(2)} km`);
  });
}

// --- 16. Categoria mais vendida por área geográfica --- //

print('\n--- CONSULTA 16: Categoria Mais Vendida por Região ---');
// Define área geográfica (região Sudeste: SP, RJ, MG)
const targetRegion = ["SP", "RJ", "MG"];

print(`Analisando vendas na região: ${targetRegion.join(", ")}`);

const categoryByRegion = db.orders.aggregate([
  {
    // Lookup para obter dados do comprador
    $lookup: {
      from: "users",
      localField: "userId",
      foreignField: "_id",
      as: "buyer"
    }
  },
  {
    $unwind: "$buyer"
  },
  {
    // Filtra apenas compradores da região especificada
    $match: {
      "buyer.address.State": { $in: targetRegion }
    }
  },
  {
    // Desconstrói produtos do pedido
    $unwind: "$products"
  },
  {
    // Lookup para obter dados do produto
    $lookup: {
      from: "products",
      localField: "products.productId",
      foreignField: "_id",
      as: "productInfo"
    }
  },
  {
    $unwind: "$productInfo"
  },
  {
    // Lookup para obter dados da categoria
    $lookup: {
      from: "categories",
      localField: "productInfo.categoryId",
      foreignField: "_id",
      as: "category"
    }
  },
  {
    $unwind: "$category"
  },
  {
    // Agrupa por categoria
    $group: {
      _id: "$category._id",
      categoryName: { $first: "$category.name" },
      totalQuantitySold: { $sum: "$products.quantity" },
      totalRevenue: {
        $sum: { $multiply: ["$products.quantity", "$products.price"] }
      },
      totalOrders: { $sum: 1 }
    }
  },
  {
    // Ordena por quantidade vendida
    $sort: { totalQuantitySold: -1 }
  }
]).toArray();

print(`✓ Categorias mais vendidas na região ${targetRegion.join(", ")}:`);
categoryByRegion.forEach((category, index) => {
  print(`  ${index + 1}. ${category.categoryName}:`);
  print(`     Quantidade Vendida: ${category.totalQuantitySold} unidades`);
  print(`     Receita Total: R$ ${category.totalRevenue.toFixed(2)}`);
  print(`     Número de Pedidos: ${category.totalOrders}`);
});

if (categoryByRegion.length > 0) {
  print(`\n  🏆 Categoria mais vendida: ${categoryByRegion[0].categoryName}`);
}

print('\n==============================================');
print('===     CONSULTAS CONCLUÍDAS COM SUCESSO   ===');
print('==============================================\n');

// Script concluído - sem retorno no painel de resultados
void 0;