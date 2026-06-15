import os
import re


"""

[ 사용 가이드 ]
1. 'PROBLEMS.md' 문제 업데이트 되어있는지 확인!
2. [✅중요] (90번째 줄) 'save_path' 변수를 본인의 폴더 경로로 수정
   예: save_path = "./김진효/week01"
3. 터미널에서 'python algo_problem_file.py'를 입력하여 실행

문제 발생 시 말해주세요

"""


def create_files_from_this_week(file_path, target_path):
    if not os.path.exists(file_path):
        print(f"❌ {file_path} 파일이 없습니다.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        full_content = f.read()

    # 1. 섹션 추출 (id="this-week")
    start_match = re.search(r'<details[^>]*id=["\']this-week["\'][^>]*>', full_content)
    if not start_match:
        print("🔍 'this-week' 섹션을 찾을 수 없습니다.")
        return

    start_idx = start_match.start()
    end_tag = '</details>'
    end_idx = full_content.find(end_tag, start_idx)
    target_section = full_content[start_idx:end_idx]

    # 2. 타겟 경로 생성 (없으면 생성)
    if not os.path.exists(target_path):
        os.makedirs(target_path, exist_ok=True)
        print(f"📁 폴더 생성 완료: {target_path}")

    print(f"📅 [이번 주 문제] 분석 및 '{target_path}'에 파일 생성 중...")

    # 3. 줄 단위 분석
    lines = target_section.split("\n")
    found_count = 0

    for line in lines:
        line = line.strip()
        if line.startswith("|") and "---" not in line and "난이도" not in line and "summary" not in line:
            parts = [p.strip() for p in line.split("|") if p.strip()]

            if len(parts) < 3:
                continue

            prob_num = parts[1]
            raw_title_link = parts[2]
            
            link_match = re.search(r'\[([^\]]+)\]\((https?://[^\)]+)\)', raw_title_link)
            
            if link_match:
                title = link_match.group(1).strip()
                url = link_match.group(2).strip()
                
                clean_title = "".join([c for c in title if c.isalnum() or c in (' ', '_')]).strip().replace(" ", "_")
                f_name = f"{prob_num}_{clean_title}.py"
                
                # [핵심] 지정된 경로와 파일명 결합
                full_file_path = os.path.join(target_path, f_name)

                if not os.path.exists(full_file_path):
                    with open(full_file_path, "w", encoding="utf-8") as f_new:
                        f_new.write(f"# 문제: {title}\n")
                        f_new.write(f"# URL: {url}\n\n")
                        f_new.write("def solution():\n    pass\n")
                    print(f"✅ 생성 완료: {full_file_path}")
                else:
                    print(f"🟡 이미 존재: {f_name} (스킵)")
                
                found_count += 1

    print(f"\n✨ 총 {found_count}개의 파일 처리를 완료했습니다.")

if __name__ == "__main__":

    # 문제 목록 파일
    md_file = "PROBLEMS.md"
    
    # 파일을 생성할 경로 입력
    save_path = ("./작성자/주차")
    
    create_files_from_this_week(md_file, save_path)