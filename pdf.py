import PyPDF2

def merge_pdfs(paths, output):
    pdf_merger = PyPDF2.PdfMerger()
    
    for path in paths:
        pdf_merger.append(path)
        
    with open(output, 'wb') as f:
        pdf_merger.write(f)

# 사용 예시
files = ['./스캔1.pdf', './프로필.pdf']
merge_pdfs(files, './merged_result.pdf')