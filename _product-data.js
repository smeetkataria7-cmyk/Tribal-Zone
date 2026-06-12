var PRODUCTS = [
  {
    id: 'TZ4361-008',
    title: 'Gold Kundan Cluster Studs',
    category: 'Earrings',
    price: 399,
    compareAtPrice: 458,
    featured: false,
    image1: 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&q=70',
    image2: 'https://images.unsplash.com/photo-1515377905703-c511b6b891f1?w=500&q=70'
  },
  {
    id: 'TZ4357-12',
    title: 'Crystal Drop Earrings',
    category: 'Earrings',
    price: 599,
    compareAtPrice: 688,
    featured: false,
    image1: 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&q=70',
    image2: 'https://images.unsplash.com/photo-1515377905703-c511b6b891f1?w=500&q=70'
  },
  {
    id: 'TZ4357-19',
    title: 'White Pearl Studs',
    category: 'Earrings',
    price: 599,
    compareAtPrice: 688,
    featured: false,
    image1: 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&q=70',
    image2: 'https://images.unsplash.com/photo-1515377905703-c511b6b891f1?w=500&q=70'
  },
  {
    id: 'TZ4383-1',
    title: 'Antique Gold Jhumka',
    category: 'Earrings',
    price: 699,
    compareAtPrice: 803,
    featured: false,
    image1: 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&q=70',
    image2: 'https://images.unsplash.com/photo-1515377905703-c511b6b891f1?w=500&q=70'
  },
  {
    id: 'TZ4383-5',
    title: 'Kundan Drop Earring',
    category: 'Earrings',
    price: 699,
    compareAtPrice: 803,
    featured: false,
    image1: 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&q=70',
    image2: 'https://images.unsplash.com/photo-1515377905703-c511b6b891f1?w=500&q=70'
  },
  {
    id: 'TZ5201-001',
    title: 'Crystal Pendant Necklace',
    category: 'Necklaces',
    price: 899,
    compareAtPrice: 1033,
    featured: false,
    image1: 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&q=70',
    image2: 'https://images.unsplash.com/photo-1515377905703-c511b6b891f1?w=500&q=70'
  },
  {
    id: 'TZ5202-001',
    title: 'Layered Chain Necklace',
    category: 'Necklaces',
    price: 799,
    compareAtPrice: 918,
    featured: false,
    image1: 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&q=70',
    image2: 'https://images.unsplash.com/photo-1515377905703-c511b6b891f1?w=500&q=70'
  },
  {
    id: 'TZ5203-001',
    title: 'Kundan Temple Necklace',
    category: 'Necklaces',
    price: 1299,
    compareAtPrice: 1493,
    featured: false,
    image1: 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&q=70',
    image2: 'https://images.unsplash.com/photo-1515377905703-c511b6b891f1?w=500&q=70'
  },
  {
    id: 'TZ6101-001',
    title: 'Crystal Beaded Bracelet',
    category: 'Bangles',
    price: 499,
    compareAtPrice: 573,
    featured: false,
    image1: 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&q=70',
    image2: 'https://images.unsplash.com/photo-1515377905703-c511b6b891f1?w=500&q=70'
  },
  {
    id: 'TZ6102-001',
    title: 'Gold Bangle Set',
    category: 'Bangles',
    price: 799,
    compareAtPrice: 918,
    featured: false,
    image1: 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&q=70',
    image2: 'https://images.unsplash.com/photo-1515377905703-c511b6b891f1?w=500&q=70'
  },
  {
    id: 'TZ6103-001',
    title: 'Antique Silver Bangle',
    category: 'Bangles',
    price: 599,
    compareAtPrice: 688,
    featured: false,
    image1: 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&q=70',
    image2: 'https://images.unsplash.com/photo-1515377905703-c511b6b891f1?w=500&q=70'
  },
  {
    id: 'TZ7101-001',
    title: 'Pearl Maang Tikka',
    category: 'Maang Tikka',
    price: 799,
    compareAtPrice: 918,
    featured: false,
    image1: 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&q=70',
    image2: 'https://images.unsplash.com/photo-1515377905703-c511b6b891f1?w=500&q=70'
  },
  {
    id: 'TZ7102-001',
    title: 'Kundan Maang Tikka',
    category: 'Maang Tikka',
    price: 999,
    compareAtPrice: 1148,
    featured: false,
    image1: 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&q=70',
    image2: 'https://images.unsplash.com/photo-1515377905703-c511b6b891f1?w=500&q=70'
  },
  {
    id: 'TZ8101-001',
    title: 'Gold Statement Ring',
    category: 'Rings',
    price: 599,
    compareAtPrice: 688,
    featured: false,
    image1: 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&q=70',
    image2: 'https://images.unsplash.com/photo-1515377905703-c511b6b891f1?w=500&q=70'
  },
  {
    id: 'TZ8102-001',
    title: 'Aries Zodiac Ring',
    category: 'Rings',
    price: 699,
    compareAtPrice: 803,
    featured: false,
    image1: 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&q=70',
    image2: 'https://images.unsplash.com/photo-1515377905703-c511b6b891f1?w=500&q=70'
  },
  {
    id: 'TZ9201-ARIES',
    title: 'Aries Zodiac Pendant',
    category: 'Zodiac',
    price: 699,
    compareAtPrice: 803,
    featured: false,
    image1: 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&q=70',
    image2: 'https://images.unsplash.com/photo-1515377905703-c511b6b891f1?w=500&q=70'
  },
  {
    id: 'TZ9202-TAURUS',
    title: 'Taurus Zodiac Pendant',
    category: 'Zodiac',
    price: 699,
    compareAtPrice: 803,
    featured: false,
    image1: 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&q=70',
    image2: 'https://images.unsplash.com/photo-1515377905703-c511b6b891f1?w=500&q=70'
  },
];