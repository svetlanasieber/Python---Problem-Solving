def process_commands():
   
    genres = input().split(' | ')

    while True:
        command = input().split()

       
        if command[0] == "Stop!":
            break

        action = command[0]

        
        if action == "Join":
            genre = command[1]
            if genre not in genres:
                genres.append(genre)

        elif action == "Drop":
            genre = command[1]
            if genre in genres:
                genres.remove(genre)

        elif action == "Replace":
            old_genre, new_genre = command[1], command[2]
            if old_genre in genres and new_genre not in genres:
                index = genres.index(old_genre)
                genres[index] = new_genre

       
        elif action == "Prefer":
            index1, index2 = int(command[1]), int(command[2])
            if 0 <= index1 < len(genres) and 0 <= index2 < len(genres):
                genres[index1], genres[index2] = genres[index2], genres[index1]

   
    print(' '.join(genres))

process_commands()
