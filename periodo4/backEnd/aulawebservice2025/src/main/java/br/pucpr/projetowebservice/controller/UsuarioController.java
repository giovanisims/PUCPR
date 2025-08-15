package br.pucpr.projetowebservice.controller;

import br.pucpr.projetowebservice.dto.UsuarioDTO;
import jakarta.websocket.server.PathParam;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/api/v1/usuario")
public class UsuarioController {

    private List<UsuarioDTO> usuarios = new ArrayList<>();

    @PostMapping
    public ResponseEntity<UsuarioDTO> save(@RequestBody UsuarioDTO usuarioDTO) {
        usuarioDTO.setId(1);
        usuarios.add(usuarioDTO);
        return ResponseEntity.status(HttpStatus.CREATED).body(usuarioDTO);
    }

    @GetMapping
    public List<UsuarioDTO> findAll() {
        return usuarios;
    }

    @PutMapping("/{id}")
    public UsuarioDTO update(@PathVariable("id") Integer id, @RequestBody UsuarioDTO usuarioDTO) {
        usuarioDTO.setId(id);
        return usuarioDTO;
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable("id") Integer id) {
    }

}
