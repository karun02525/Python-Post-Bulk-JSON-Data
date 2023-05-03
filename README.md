# Python-Post-Bulk-JSON-Data
Python  Django Post Bulk JSON Data

@api_view(['POST'])
def create_bulk(request):
    items = request.data.get('items')
    '''items = [
       {
      "name": "VNS Bokari School",
      "city": "Bokaro",
      "age": 23
    },
    {
      "name": "Dhar SViS  School",
      "city": "Dhanbad",
      "age": 22
    }] '''
    bulk_list = []
    for item in items:
        bulk_list.append(Teacher(name=item.get('name'),age=item.get('age'),city=item.get('city')))
    Teacher.objects.bulk_create(bulk_list)    
    return Response({'status':True,'message':'all data create successfull'},status=status.HTTP_201_CREATED)
  
    
