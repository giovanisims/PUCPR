package br.pucpr.projetowebservice.dto;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import lombok.Data;

@Data
public class UsuarioDTO {

    private Integer id;
    @NotBlank
    @NotNull(message = "ERROR-MESSAGE-001")
    private String nome;
    @Email
    private String email;

}
