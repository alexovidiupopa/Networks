#include <sys/socket.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <netinet/ip.h> 
char msg[20];
char receive[20];
struct sockaddr_in soc;
int sfd;
int rc;

int main(int argc, char argv[]){
	sfd = socket(AF_INET, SOCK_STREAM, 0);
	
	soc.sin_family = AF_INET;
	soc.sin_addr.s_addr = inet_addr("172.30.116.45");
	soc.sin_port = htons(4444);

	rc = connect(sfd, (struct sockaddr *)&soc, sizeof(soc));
	
	while (1){
		printf("Enter message:");
		fgets(msg,sizeof(msg),stdin);
	//printf(msg);
		rc = send(sfd, msg, strlen(msg),0);	
		rc = recv(sfd, receive, 20, 0);
		printf(receive);	
	}
	return 0;
}
