import csv
import json
import os

def convertir_csv_a_json():
    print("🔄 CONVERTIDOR CSV A JSON (respeta stock real)")
    print("=" * 45)
    
    csv_file = input("\n📁 Nombre del archivo CSV: ").strip()
    
    if not os.path.exists(csv_file):
        print(f"❌ Error: No se encuentra '{csv_file}'")
        return
    
    datos = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        
        for fila in lector:
            disponible_raw = fila.get("Available", "0")
            
            # Convertir a número (entero o flotante)
            try:
                cantidad = float(disponible_raw)
            except:
                cantidad = 0
            
            # Regla: si cantidad es mayor a 0 → disponible
            if cantidad > 0:
                disponible = 1
            else:
                disponible = 0
            
            nuevo_registro = {
                "SKU": fila.get("Name", ""),
                "Description": fila.get("Description", ""),
                "Available": disponible
            }
            datos.append(nuevo_registro)
    
    # Guardar JSON
    json_file = csv_file.replace('.csv', '.json')
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)
    
    # Mostrar estadísticas
    disponibles = sum(1 for p in datos if p['Available'] == 1)
    no_disponibles = sum(1 for p in datos if p['Available'] == 0)
    
    print(f"\n✅ ¡Listo! {len(datos)} productos guardados en {json_file}")
    print(f"📊 Productos disponibles (stock > 0): {disponibles}")
    print(f"📊 Productos no disponibles (stock = 0): {no_disponibles}")

if __name__ == "__main__":
    convertir_csv_a_json()