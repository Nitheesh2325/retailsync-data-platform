import os
import time
from logger import log
start = time.time()

log("=" * 60)
log(" RETAILSYNC DATA PIPELINE ")
log("=" * 60)

log("\nStep 1 - Generating Orders...")
os.system("python src/generate_enterprise_orders.py")

log("\nStep 2 - Loading SQLite...")
os.system("python src/load_to_sqlite.py")

log("\nStep 3 - Running SQL Analytics...")
os.system("python src/sql_analytics.py")
log("\nStep 4 - Generating Dashboard...")
os.system("python src/dashboard.py")
os.startfile("reports/charts/monthly_revenue.png")

end = time.time()

log("\nPipeline Completed Successfully!")
log(f"Total Execution Time: {round(end - start, 2)} seconds")