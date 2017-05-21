#include<iostream>
#include<stdio.h>
#include<time.h>
#include<algorithm>
#include<string.h>
using namespace std;
void print(char a[],int length){
for(int i=0;i<length;i++) cout<<a[i];
cout<<'\n';
}
void deal_with_question(char filename[])
{
cin.sync_with_stdio(false);
freopen(filename,"r",stdin);
freopen("questions.txt","w",stdout);

string str;
char tmp;
int i=0;
while(cin.get(tmp))
{
    if(tmp!='\t') continue;
    else i++;
    i%=2;
    if(i==1){
    cin>>str;
    cout<<str<<'\n';
    }
}
  return ;
}
void deal_with_document(char filename[])
{
cin.sync_with_stdio(false);
freopen(filename,"r",stdin);
freopen("document.txt","w",stdout);

string str;
char tmp;
int i=0;
while(cin.get(tmp))
{
    if(tmp!='\t') continue;
    else i++;
    i%=2;
    if(i==0){
    cin>>str;
    cout<<str<<'\n';
    }
}
  return ;
}

void synthesize_question_document(char filename[])
{
cin.sync_with_stdio(false);
freopen(filename,"r",stdin);
freopen("question_document.txt","w",stdout);

string str;
string current_question;
char tmp;
int i=0;
while(cin.get(tmp))
{
    if(tmp!='\t') continue;
    else i++;

    i%=2;

    if(i==1){
    cin>>str;

    if(str!=current_question)
    {
        cout<<str<<'\n';
        current_question=str;
    }

    }
    else {
    cin>>str;
    cout<<str<<'\n';
    }

}
return ;
}


int main(){
char filename[50];
cin>>filename;

/**************以下代码均已除去 [0] [1] label*****************/

/*************问题****************/

//deal_with_question(filename);


/*************文章****************/

//deal_with_document(filename);

/*************一行问题 + 文章****************/

synthesize_question_document(filename);

}
