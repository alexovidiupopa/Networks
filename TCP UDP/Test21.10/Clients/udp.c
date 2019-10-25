#include <netinet/ip.h>
#include <string.h>
char buf[8] = "hello";
int sfd;
struct sockaddr_in soc;
int len = sizeof(struct sockaddr_in);
int main (int argc, char argv[])
{
	char *h="abcdeo";
	int n=strlen(h);
	int a=10,b=20;
	
	sfd=socket(AF_INET, SOCK_DGRAM, 0);    
	soc.sin_family=AF_INET;
	soc.sin_port=htons(5555);
	soc.sin_addr.s_addr=inet_addr("172.30.116.45");	 
	
	sendto (sfd,h,n,0,&soc,sizeof(struct sockaddr_in));
	
	int answer = 0;

	recvfrom(sfd, &answer, sizeof(int),0,&soc, &len);
	
	printf("The word has: %d vowels.\n", answer);
	return 0;
}
