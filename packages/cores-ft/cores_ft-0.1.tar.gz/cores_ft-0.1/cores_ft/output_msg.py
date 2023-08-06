def mount_msg_output(freq, temp):
    msg = []
    for (k, f), t in zip(freq.items(), temp.values()):
        msg.append(f'| {k} : {f:.4f} Ghz {t} |')
    msg = '\n'.join(msg)

    return msg
