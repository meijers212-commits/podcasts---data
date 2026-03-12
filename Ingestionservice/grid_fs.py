import gridfs

def save_file_mongodb(logger, mongo_db, file_name, file_path):
    try:
        # Create a GridFS object for the selected database
        fs = gridfs.GridFS(mongo_db)

        with open(file_path, 'rb') as file_data:
            fs.put(file_data, filename=file_name)

        logger.info(f"file: {file_name}saved to mongo")
        
    except Exception as e:
        logger.error(e)



