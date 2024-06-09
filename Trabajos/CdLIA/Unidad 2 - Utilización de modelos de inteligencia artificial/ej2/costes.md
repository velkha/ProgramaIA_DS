### 1. **Costos de Infraestructura en Azure**

#### a. **Azure Machine Learning**
- **Azure Machine Learning Service Workspace**: $9.9/mes

#### b. **Computación**
- **Virtual Machines** (para entrenamiento del modelo): 
  - Azure DSv3-series (D8s v3) VM: $0.40/hora
  - Asumiendo 100 horas de uso al mes: $40

#### c. **Almacenamiento**
- **Azure Blob Storage**: $0.0208/GB al mes
  - Estimación de 100 GB de almacenamiento: $2.08/mes

#### d. **Azure Databricks**
- **DBU (Databricks Unit) por hora**:
  - Standard plan: $0.25/DBU/hora
  - Asumiendo 100 horas al mes: $25

#### e. **Azure Kubernetes Service (AKS)**
- **AKS Cluster**: Los costos dependen de los nodos utilizados.
  - Suponiendo un pequeño clúster con 3 nodos: $0.096/nodo/hora
  - Asumiendo 100 horas de uso al mes: $28.8

#### f. **Azure Cognitive Services (Text Analytics API)**
- **Text Analytics**: $2 por 1,000 llamadas de API
  - Estimación de 50,000 llamadas al mes: $100

### 2. **Costos de Personal**

#### a. **Ingeniero de Datos**
- Salario promedio: $8,000/mes

#### b. **Científico de Datos**
- Salario promedio: $9,000/mes

#### c. **Desarrollador**
- Salario promedio: $7,000/mes

#### d. **Analista de Negocios**
- Salario promedio: $6,000/mes

### 3. **Costos Totales**

#### a. **Costos de Infraestructura Mensuales**
| Servicio                         | Costo Estimado    |
|----------------------------------|-------------------|
| Azure ML Service Workspace       | $9.9              |
| VM para Entrenamiento (100 hrs)  | $40               |
| Almacenamiento (100 GB)          | $2.08             |
| Azure Databricks (100 hrs)       | $25               |
| AKS Cluster (3 nodos, 100 hrs)   | $28.8             |
| Text Analytics API (50,000 calls)| $100              |
| **Total Infraestructura**        | **$205.78**       |

#### b. **Costos de Personal Mensuales**
| Rol                   | Salario Mensual |
|-----------------------|-----------------|
| Ingeniero de Datos    | $8,000          |
| Científico de Datos   | $9,000          |
| Desarrollador         | $7,000          |
| Analista de Negocios  | $6,000          |
| **Total Personal**    | **$30,000**     |

#### c. **Costo Total del Proyecto (Mensual)**
| Categoría             | Costo Estimado  |
|-----------------------|-----------------|
| Infraestructura       | $205.78         |
| Personal              | $30,000         |
| **Total**             | **$30,205.78**  |

### Estimación para un Proyecto de 6 Meses

Si asumimos que el proyecto durará seis meses, la estimación total sería:

| Categoría             | Costo Total 6 Meses |
|-----------------------|---------------------|
| Infraestructura       | $1,234.68           |
| Personal              | $180,000            |
| **Total**             | **$181,234.68**     |

### Consideraciones Adicionales
- **Entrenamiento y ajuste del modelo**: Los costos pueden variar dependiendo de la complejidad y la cantidad de datos utilizados.
- **Despliegue y mantenimiento**: Una vez desplegado, los costos de mantenimiento y actualizaciones deben considerarse.
- **Licencias y suscripciones**: Revisar posibles licencias adicionales que puedan ser necesarias.
