package pl.edu.pk.ztp.dto;


public class RentDTOConv {
    public static Rent convert(RentDTO rentDTO) {
        Rent rent = new Rent();
        rent.setRental(rentDTO.getRentalDate());
        rent.setReturnDate(rentDTO.getReturnDate());
        rent.setBook(rentDTO.getBook());
        return rent;
    }

    public static RentDTO convert(Rent rent) {
        return RentDTO.builder()
                .book(rent.getBook())
                .rentalDate(rent.getRental())
                .returnDate(rent.getReturnDate())
                .user(UserDTOConv.convert(rent.getUser()))
                .build();
    }

}
