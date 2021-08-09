dataset = project.datasets.get(dataset_name='MyData9821')
project = dl.projects.get(project_name='YakirsProject9821')
dataset.add_label(label_name='auto', color=(34, 6, 231), attributes=['big', 'small'])
dataset.items.upload(local_path="C:\Users\Yakir\OneDrive\Desktop\BMX.jpg")