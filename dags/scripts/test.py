from pyspark.sql import SparkSession
import os

# 현재 디렉토리 경로
current_dir = os.getcwd()

# 입력 및 출력 파일 경로 설정
input_file = os.path.join(current_dir, "input.csv")
output_dir = os.path.join(current_dir, "output")

# SparkSession 생성
spark = SparkSession.builder \
    .appName("Simple PySpark Example") \
    .master("local[*]") \
    .getOrCreate()

# 샘플 CSV 데이터 생성
with open(input_file, "w") as f:
    f.write("name,age\n")
    f.write("Alice,29\n")
    f.write("Bob,35\n")
    f.write("Charlie,30\n")

# CSV 파일 읽기
df = spark.read.csv(input_file, header=True, inferSchema=True)

# 데이터 프레임의 스키마 및 첫 5개의 행 출력
df.printSchema()
df.show()

# 간단한 데이터 변환 (예: 'age' 열에서 30세 이상인 사람만 필터링)
filtered_df = df.filter(df["age"] >= 30)

# 결과 출력
filtered_df.show()

# 결과를 현재 디렉토리에 다시 CSV 파일로 저장
filtered_df.write.csv(output_dir, header=True, mode='overwrite')

# Spark 세션 종료
spark.stop()

# 출력 파일 확인
print(f"Filtered output saved in: {output_dir}")
