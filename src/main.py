import os, shutil
from block_markdown import markdown_to_html_node, extract_title

def main():
    
    shutil.rmtree("/root/pr/web/static")

    def copy_contents(source_dir, target_dir):
        
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)

        if os.path.isdir(source_dir):
            files = os.listdir(source_dir)
            if len(files) > 0:
                for file in files:
                    file_path = os.path.join(source_dir, file)
                    target_path = os.path.join(target_dir, file)
                    print(os.path.isfile(file_path))
                    if os.path.isfile(file_path):
                        print(f"File path: {file_path}")
                        shutil.copy(file_path, target_dir)
                    else:
                        print(f"Directory path: {file_path}")
                        if not os.path.exists(target_path):
                            os.mkdir(target_path)
                        copy_contents(file_path, target_path)

    def create_page(from_path, template_path, dest_path):
        print(f"Generating page from {from_path} to {dest_path} using {template_path}")

        markdown_file = open(from_path, "r")
        template_file = open(template_path, "r")
        markdown = markdown_file.read()
        template = template_file.read()

        html = markdown_to_html_node(markdown).to_html()
        title = extract_title(markdown)

        template = template.replace("Title", title)
        template = template.replace("Content", html)

        with open(dest_path, "w") as f:
            print("Dest path :", dest_path)
            f.write(template)
        
    def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
        
        if os.path.isdir(dir_path_content):
            files = os.listdir(dir_path_content)
            for file in files:
                file_path = os.path.join(dir_path_content, file)
                dest_path = os.path.join(dest_dir_path, file)
                if os.path.isfile(file_path):
                    if file.endswith(".md"):
                        dest_path = dest_path.replace(".md", ".html")
                        create_page(file_path, template_path, dest_path)
                else:
                    if not os.path.exists(dest_path):
                        os.mkdir(dest_path)
                    generate_page_recursive(file_path, template_path, dest_path)

    copy_contents("/root/pr/web/public", "/root/pr/web/static")


    generate_page_recursive("/root/pr/web/content", "/root/pr/web/template.html", "/root/pr/web/public")

    
    


    

            


main()


