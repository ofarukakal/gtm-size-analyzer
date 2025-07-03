import json
import csv

def analyze_gtm_container_full(json_file_path):
    """GTM konteyner JSON dosyasını tam analiz eder ve tüm öğeleri listeler"""
    
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        container_version = data.get('containerVersion', {})
        
        # Tags (Etiketler) analizi
        tags = container_version.get('tag', [])
        tag_analysis = []
        
        for tag in tags:
            tag_info = {
                'name': tag.get('name', 'Unknown'),
                'type': tag.get('type', 'Unknown'),
                'size': len(json.dumps(tag, ensure_ascii=False)),
                'parameters': len(tag.get('parameter', [])),
                'triggers': len(tag.get('firingTriggerId', [])),
                'tag_id': tag.get('tagId', 'Unknown'),
                'firing_triggers': ', '.join(tag.get('firingTriggerId', [])) if tag.get('firingTriggerId') else 'None'
            }
            tag_analysis.append(tag_info)
        
        # Triggers (Tetikleyiciler) analizi
        triggers = container_version.get('trigger', [])
        trigger_analysis = []
        
        for trigger in triggers:
            trigger_info = {
                'name': trigger.get('name', 'Unknown'),
                'type': trigger.get('type', 'Unknown'),
                'size': len(json.dumps(trigger, ensure_ascii=False)),
                'conditions': len(trigger.get('filter', [])),
                'trigger_id': trigger.get('triggerId', 'Unknown')
            }
            trigger_analysis.append(trigger_info)
        
        # Variables (Değişkenler) analizi
        variables = container_version.get('variable', [])
        variable_analysis = []
        
        for variable in variables:
            variable_info = {
                'name': variable.get('name', 'Unknown'),
                'type': variable.get('type', 'Unknown'),
                'size': len(json.dumps(variable, ensure_ascii=False)),
                'parameters': len(variable.get('parameter', [])),
                'variable_id': variable.get('variableId', 'Unknown')
            }
            variable_analysis.append(variable_info)
        
        # Boyutlarına göre sırala
        tag_analysis.sort(key=lambda x: x['size'], reverse=True)
        trigger_analysis.sort(key=lambda x: x['size'], reverse=True)
        variable_analysis.sort(key=lambda x: x['size'], reverse=True)
        
        # Konteyner bilgileri
        container_info = container_version.get('container', {})
        print("=" * 100)
        print(f"GTM KONTEYNER DETAYLI ANALİZİ")
        print(f"Konteyner Adı: {container_info.get('name', 'Unknown')}")
        print(f"Konteyner ID: {container_info.get('publicId', 'Unknown')}")
        print(f"Account ID: {container_info.get('accountId', 'Unknown')}")
        print("=" * 100)
        
        # TÜM ETİKETLER LİSTESİ
        print(f"\n📋 TÜM ETİKETLER (TAGS) - Toplam: {len(tag_analysis)}")
        print("=" * 100)
        print(f"{'#':<4} {'Etiket Adı':<50} {'Tip':<20} {'Boyut':<8} {'Param':<6} {'Tetik':<6} {'Tag ID':<8}")
        print("-" * 100)
        
        for i, tag in enumerate(tag_analysis, 1):
            name = tag['name'][:47] + "..." if len(tag['name']) > 50 else tag['name']
            type_str = tag['type'][:17] + "..." if len(tag['type']) > 20 else tag['type']
            print(f"{i:<4} {name:<50} {type_str:<20} {tag['size']:<8} {tag['parameters']:<6} {tag['triggers']:<6} {tag['tag_id']:<8}")
        
        # TÜM TETİKLEYİCİLER LİSTESİ
        print(f"\n🎯 TÜM TETİKLEYİCİLER (TRIGGERS) - Toplam: {len(trigger_analysis)}")
        print("=" * 100)
        print(f"{'#':<4} {'Tetikleyici Adı':<50} {'Tip':<20} {'Boyut':<8} {'Koşul':<6} {'Trigger ID':<10}")
        print("-" * 100)
        
        for i, trigger in enumerate(trigger_analysis, 1):
            name = trigger['name'][:47] + "..." if len(trigger['name']) > 50 else trigger['name']
            type_str = trigger['type'][:17] + "..." if len(trigger['type']) > 20 else trigger['type']
            print(f"{i:<4} {name:<50} {type_str:<20} {trigger['size']:<8} {trigger['conditions']:<6} {trigger['trigger_id']:<10}")
        
        # TÜM DEĞİŞKENLER LİSTESİ
        print(f"\n🔧 TÜM DEĞİŞKENLER (VARIABLES) - Toplam: {len(variable_analysis)}")
        print("=" * 100)
        print(f"{'#':<4} {'Değişken Adı':<50} {'Tip':<20} {'Boyut':<8} {'Param':<6} {'Variable ID':<12}")
        print("-" * 100)
        
        for i, variable in enumerate(variable_analysis, 1):
            name = variable['name'][:47] + "..." if len(variable['name']) > 50 else variable['name']
            type_str = variable['type'][:17] + "..." if len(variable['type']) > 20 else variable['type']
            print(f"{i:<4} {name:<50} {type_str:<20} {variable['size']:<8} {variable['parameters']:<6} {variable['variable_id']:<12}")
        
        # CSV dosyaları oluştur
        print(f"\n📄 CSV Dosyaları Oluşturuluyor...")
        
        # Etiketler CSV
        with open('gtm_tags_analysis.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['sira', 'ad', 'tip', 'boyut_byte', 'parametre_sayisi', 'tetikleyici_sayisi', 'tag_id', 'firing_triggers']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i, tag in enumerate(tag_analysis, 1):
                writer.writerow({
                    'sira': i,
                    'ad': tag['name'],
                    'tip': tag['type'],
                    'boyut_byte': tag['size'],
                    'parametre_sayisi': tag['parameters'],
                    'tetikleyici_sayisi': tag['triggers'],
                    'tag_id': tag['tag_id'],
                    'firing_triggers': tag['firing_triggers']
                })
        
        # Tetikleyiciler CSV
        with open('gtm_triggers_analysis.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['sira', 'ad', 'tip', 'boyut_byte', 'kosul_sayisi', 'trigger_id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i, trigger in enumerate(trigger_analysis, 1):
                writer.writerow({
                    'sira': i,
                    'ad': trigger['name'],
                    'tip': trigger['type'],
                    'boyut_byte': trigger['size'],
                    'kosul_sayisi': trigger['conditions'],
                    'trigger_id': trigger['trigger_id']
                })
        
        # Değişkenler CSV
        with open('gtm_variables_analysis.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['sira', 'ad', 'tip', 'boyut_byte', 'parametre_sayisi', 'variable_id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i, variable in enumerate(variable_analysis, 1):
                writer.writerow({
                    'sira': i,
                    'ad': variable['name'],
                    'tip': variable['type'],
                    'boyut_byte': variable['size'],
                    'parametre_sayisi': variable['parameters'],
                    'variable_id': variable['variable_id']
                })
        
        print("✅ gtm_tags_analysis.csv dosyası oluşturuldu")
        print("✅ gtm_triggers_analysis.csv dosyası oluşturuldu")
        print("✅ gtm_variables_analysis.csv dosyası oluşturuldu")
        
        # TOP 10 özetleri
        print(f"\n🏆 EN BÜYÜK 10 ETİKET")
        print("-" * 80)
        for i, tag in enumerate(tag_analysis[:10], 1):
            print(f"{i:2}. {tag['name'][:60]} ({tag['size']:,} byte)")
        
        print(f"\n🏆 EN BÜYÜK 10 TETİKLEYİCİ")
        print("-" * 80)
        for i, trigger in enumerate(trigger_analysis[:10], 1):
            print(f"{i:2}. {trigger['name'][:60]} ({trigger['size']:,} byte)")
        
        print(f"\n🏆 EN BÜYÜK 10 DEĞİŞKEN")
        print("-" * 80)
        for i, variable in enumerate(variable_analysis[:10], 1):
            print(f"{i:2}. {variable['name'][:60]} ({variable['size']:,} byte)")
        
        print("\n" + "=" * 100)
        
    except FileNotFoundError:
        print(f"Hata: '{json_file_path}' dosyası bulunamadı.")
    except json.JSONDecodeError as e:
        print(f"Hata: JSON dosyası geçersiz - {e}")
    except Exception as e:
        print(f"Beklenmeyen hata: {e}")

if __name__ == "__main__":
    json_file = "gtm-workspace.json"
    analyze_gtm_container_full(json_file)